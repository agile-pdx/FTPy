import argparse
import pysftp

def main():
    #Grab user command-line input
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', '--url')
    parser.add_argument('-u', '--username')
    args = parser.parse_args()

    #Avoid getting password from command-line argument for enhanced security
    secure_password = raw_input("Enter your password: ")

    print "Attempting to connect to " + args.url + " as '" + args.username + "'..."

    #Establish SFTP connection, if connection fails, raise exception
    try:
        sftp = pysftp.Connection(args.url, username=args.username, password=secure_password)
    except pysftp.ConnectionException:
        print "Unsuccessful attempt to connect!"
    except pysftp.AuthenticationException:
        print "Authenication failed"
    except pysftp.CredentialException:
        print "Credentials failed"
    except pysftp.SSHException:
        print "SSH Exception"
    else:
        print "Successfully connected to " + args.url
        print sftp.listdir()

    input_command = ""
    #While loop to get user commands, which will be 1 character long and start
    #with a -, and args that follow
    while input_command != '-q':
        input = raw_input("Enter a command: ")
        input_list = []
        input_list = input.split(" ", 1)
        #Checks if command and arg both present, command has - and is length of 2
        if len(input_list) > 1 and len(input_list[0]) == 2 and input_list[0].startswith("-"):
            input_command = input_list[0]
            input_arg = input_list[1]
            print input_command #Just for testing
            print input_arg # Just for testing
            action(input_command, input_arg, sftp)#To use user command
        else:
            input_command = input_list[0] # To allow -q to quit with no arg
            print "invalid entry"
            print "Usage: -command(command = single character) arg"
    print "Exiting program...Goodbye!"
            
#Add other command functions here
def action(command, arg, sftp):
    if command == "-l":
        list_dir(sftp)
    if command == "-g":
       get_file(sftp, arg)
    # add other commands, or change to switch statements

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

def get_file(sftp, arg):
    if sftp.isfile(arg):
       print "is file"
       #Add get() function
    else:
       print "That file does not exist"
       
#sftp.close()
            
if __name__ == '__main__': main()
