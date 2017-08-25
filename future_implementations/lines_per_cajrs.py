# Creating a line with the differenctial

import os
import sys


def main():
    print '-'*100
    print '-'*100
    while True:
        try:
            for i in range(150):
                if i == 75:
                    print '|' 
        except keyboardinterrupt:
            sys.exit()
    

if __name__ == "__main__":
    sys.exit(main())
