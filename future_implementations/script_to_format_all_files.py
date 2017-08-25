# This script will search for all the files inside the folder
# and will format them so that it will become easy to read the data


__author__ = "Rahul Kourav"

import os
import sys
import glob
import json


def file_operation(current_dir):
    for name in glob.glob("*.json"):
        fileobj = open(name, 'r+')
        req = json.load(fileobj)
        print req
        req = json.dump(req, indent=4, seperated=',', sort_key=True )
        print "DONE. "

def main():
    cwd = os.getcwd()
    print cwd
    file_operation(cwd)


if __name__ == "__main__":
    sys.exit(main())
