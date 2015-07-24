import argparse
import pysftp

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
    else:
        input_command = input_list[0] # To allow -q to quit with no arg
        print "invalid entry"
        print "Usage: -command(command = single character) arg"

#Add functions for various tasks
    
    
sftp.close()
