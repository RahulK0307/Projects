import sys
import re
from collections import Counter

def main(test):
    with open(r"C:\Users\rkouravx\Desktop\alldata.txt") as f:
        file_read = f.read()
        words = re.findall(test, file_read)
##        read_all = [word for word in words]
        result = Counter(words)       
        for i in result:
            if i == test:
                print 'your entered : ', i.upper(), 'Counts : ', result[i]
            


if __name__ == "__main__":
    test = raw_input("Enter your word  : ")
    sys.exit(main(test))
