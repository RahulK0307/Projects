import os
import sys
import json
import argparse

def format_json(json_data):
    try:
        json_str = json.dumps(json_data, indent=4, separators=(',', ': '))
        print "Json data has been formatted Now."
        json_obj = json.loads(json_str)
        return json_obj
    except Exception as e:
        print e.code + "Error code"
        return e


def getArgs():
    parser = argparse.ArgumentParser(description= "Process to format JSon")
    parser.add_argument('-f',
                        help='write your file name that should be formatted')
    parser.add_argument('-h',
                        help='Pass a file name to be formatted with -f')
    args = parser.parse_args()
    return args

path = r"C:\Automation\Test"

def main():
    with open(sys.argv[1], 'r') as json_file:
        file_content = json_file.read()
        format_data = format_json(file_content)
        if not os.path.exists(path):
            os.makedirs(path)
            print "Created  and Formatted"
            os.chdir(path)
        with open("test.json", 'a') as fileObj:
            final = fileObj.write(format_data)
                

if __name__ == '__main__':
    main()
    
