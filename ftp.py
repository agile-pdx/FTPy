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

#Establish SFTP connection
sftp = pysftp.Connection(args.url, username=args.username, password=secure_password)
print "Successfully connected to " + args.url
print sftp.listdir()
sftp.close()
