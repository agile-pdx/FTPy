import argparse
import pysftp
import getpass
import os

def main():
    #Grab user command-line input
    login()

    input_command = ""
    #While loop to get user commands, which will be 1 character long and start
    #with a -, and args that follow.
    while input_command != '-q':
        input = raw_input("Enter a command: ")
        input_list = []
        input_list = input.split(" ", 1)
        #Checks if command and arg both present, command has - and is length of 2
        if len(input_list) >= 1 and len(input_list[0]) == 2 and input_list[0].startswith("-"):
            input_command = input_list[0]
            if len(input_list) > 1:
                input_arg = input_list[1]
            else:
                input_arg = ""
	    #capture the returned command in order to loop
            input_command = action(input_command, input_arg, sftp)#To use user command
        else:
            input_command = input_list[0] # To allow -q to quit with no arg
            print "invalid entry"
            print "Usage: Enter a command or enter -h for help."


    sftp.close()

def login():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', '--url',type = str, help = 'SFTP server URL (linuxlab.cs.pdx.edu for PSU)')
    parser.add_argument('-u', '--username',type = str,  help = 'Desired username (Use Odin login for PSU)')
    args = parser.parse_args()

    #Set username and server address if they have yet to be set.
    if (args.url==None):
	args.url=raw_input("Enter the address of the server you wish to connect to: ")
    if (args.username==None):
        args.username=raw_input("Enter your user name for this server: ")

    #Avoid getting password from command-line argument for enhanced security. Use getpass for enhanced security.
    secure_password = getpass.getpass()
    print "Attempting to connect to " + args.url + " as '" + args.username + "'..."

    #Establish SFTP connection, if connection fails, raise exception
    try:
        sftp = pysftp.Connection(args.url, username=args.username, password=secure_password)
    except pysftp.ConnectionException:
        print "Unsuccessful attempt to connect!"
        login()
    except pysftp.AuthenticationException:
        print "Authenication failed"
        login()
    except pysftp.CredentialException:
        print "Credentials failed"
        login()
    except pysftp.SSHException:
        print "SSH Exception"
        login()
    else:
        print "Successfully connected to " + args.url
        print "\nUsage: -command(command = single character) arg or enter -h for help"

#Add other command functions here
def action(command, arg, sftp):
    if command == "-l":
        list_dir(sftp)
    elif command == "-g":
        get_file(sftp, arg)
    elif command == "-h":
	    list_commands()
    elif command == "-c":
        change_dir(sftp, arg)
    elif command == "-y":
        list_local()

    #prompt user. If the user does not want to logout, return a dummy character to be captured.
    #the character serves to continue the while loop that asks for user input.
    elif command == "-q":
	logout_resposne = ""
	logout_response = raw_input("Are you sure that you want to logout? (Y/N) ")
	while (logout_response !='Y' or logout_response!='N'):
		logout_response = logout_response[0].upper()
		if logout_response == "Y":
        		print "Closing connection."
			return "-q"
		elif logout_response == "N":
			
			return "-a"
		else:
			"invalid input please type Y to log out or N to stay retain the connection."
	
    else:
        print "invalid entry"
        print "For a list of available functions enter -h"

    # add other commands, or change to switch statements


def list_commands():
    print "Here is a list of available commands\n " \
          "-l \t list directories\n " \
          "-g \t get file \n " \
          "-h \t help\n " \
          "-q \t quit and log off\n " \
          "-c \t change directory\n " \
          "-y \t list local files\n "

def list_dir(sftp):
    dir = sftp.listdir()
    d_list = []
    f_list = []
    for i in dir:
        if sftp.isdir(i) == True:
            d_list.append(i)
        else:
            f_list.append(i)

    print "Directories:"
    for i in range(0, len(d_list)):
        
        print d_list[i],
    print "\n" + "\n" + "Files:"
    for i in range(0, len(f_list)):
   
        print f_list[i],
    print "\n"
    return (d_list, f_list)

def get_file(sftp, arg):
    found_all_items = True
    download_queue = []
    missing_items = []
    arg_items = arg.rsplit()


    #Check for missing files
    for i in range(0, len(arg_items)):
	if sftp.isfile(arg_items[i]) or sftp.isdir(arg_items[i]):
            download_queue.append(arg_items[i])
        else:
            missing_items.append(arg_items[i])
            found_all_items = False

    #Prompt to continue with transfer if files are missing
    if found_all_items == False:
        print "The following items were not found \n"
        for i in range(0, len(missing_items)):
            print missing_items[i],
        print "\n"
        input = raw_input("Would you like to download all existing items anyway (Y/N)? ")
        if input.upper() == 'N':
            return

    #create a download folder if it does not exist and go to that directory for download.
    if not os.path.isdir("downloads"):
	    os.makedirs("downloads")
	    if os.path.isdir("downloads"):
	       print "Downloads directory has been created within your current directory"
    os.chdir("downloads")
	    
    
    #Transfer all available files -- could not figure out how to use get_r... getting weird errors for files
    for i in range(0, len(download_queue)):
	print "downloading " + download_queue[i]
	if sftp.isfile(download_queue[i]):
            sftp.get(download_queue[i])
        else:
            sftp.get_r(download_queue[i], os.getcwd())
	
	print "download of " + download_queue[i] + "completed"
    os.chdir("..")
    print "Download process has been completed."

def change_dir(sftp, arg):
    try:
        sftp.cwd(arg)
        print "Directory successfully changed to " + arg
    except IOError:
        print "Path does not exist"

def list_local():
    dir = os.listdir('.')
    f_list = []
    d_list = []

    for i in dir:
        if os.path.isfile(i):
            f_list.append(i)
        else:
            d_list.append(i)
            
    print "Files: "
    print f_list
    print "Directories: "
    print d_list
            
if __name__ == '__main__': main()
