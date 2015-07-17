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
    sftp.close()
