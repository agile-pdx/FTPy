import argparse
import pysftp

#Grab user command-line input
parser = argparse.ArgumentParser()
parser.add_argument('-url', '--url')
parser.add_argument('-u', '--username')
parser.add_argument('-p', '--password')
args = parser.parse_args()

print "Attempting to connect to " + args.url + " as '" + args.username + "'..."

#TO DO: Add code to connect to server