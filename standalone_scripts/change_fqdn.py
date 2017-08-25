import re
import sys

path_to_bat = r"C:\Users\rkouravx\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start.bat"

old_fqdn = sys.argv[1]
new_fqdn = sys.argv[2]


lines = []


def read_bat_file(file_path):
    with open(file_path, 'r+') as infile:  # Reading a file in start Up
        for line in infile:
            if old_fqdn == new_fqdn:
                print >> sys.stderr, "Fqdn value is same as before , please try some different value."
                sys.exit()
            line = line.replace(old_fqdn, new_fqdn)
        lines.append(line)
   
    with open(file_path, 'w+') as outfile:  # updating the given fqdn in the start up file
        for line in lines:
            outfile.write(line)


        
# Read the bat file that contains the fqdn settings

def main():
    print >> sys.stdout, "Old Fqdn is: " + old_fqdn
    print >> sys.stdout, "New Fqdn is : " + new_fqdn
    read_bat_file(path_to_bat)


if __name__ == "__main__":
    sys.exit(main())
