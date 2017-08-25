# This will help you to get all your information that you already have saved in the same
# if it is not there then it will ask you to enter the same.

import sys
import re
import time
import random
import webbrowser


greetings = ['Hi', 'hi', 'hey', 'Hiya', 'hello', 'Hello']
greet_res = ['Thanks']
questions = ['How are you', 'hw r u', 'hw are you', 'hw r you', 'how you doing', 'hw u doing', 'how u doing', 'how are you', 'how r u']
questions_res = ['I am good', 'I am cool', 'I m doing good', 'Awesome today', 'feeling awesome']
search_word = ['google', 'yahoo', 'times of india']
exit_code = ['exit', 'bye', 'Bye', 'Good bye', 'TATA', 'Tata', 'Take care', 'quit', 'q']
whats_program = ['do you have anything new ?', 'is there anything special ?', 'something new?', 'new ?', 'whats new ?']
whats_program_res = ['Yes, Lots of things.... tell what you want me to search for', 'Yes, in which field you are interested.']
info = ['show me ', 'share it with me', 'tell me ']


# coming soon
def database_connection():
    pass


def open_web_browser(url):
    new = 2
    webbrowser.open(url, new=new)


def main():
    person_name = raw_input('Enter your name to inetract with me  :-) \n')
    print 'Hi !', person_name, ' -> This is Sandy.'
    while True:
        person_in = raw_input('>>> ')
        if person_in in greetings:
            print '>>>', random.choice(greetings)

        if person_in in questions:
            print '>>>', random.choice(questions_res), ', Tell me something about u ? '

        if person_in in questions_res:
            # print '>>>', random.choice(greet_res)
            print '>>>', "Thats good :-) ,  so how can i help you ?? "

        if person_in in whats_program:
            print '>>>', random.choice(whats_program_res)

        if person_in in search_word:
            print '>>>', "Searching for you..... Trying to get the Latest data/information based on the search...."
            if person_in == "google":
                open_web_browser('https://www.google.co.in/')
                print '>>>', "Opeining 'google' as per request...."
            elif person_in == "yahoo":
                open_web_browser('https://in.yahoo.com/')
                print '>>>', "Opeining 'yahoo' as per request...."
            elif person_in == "times of india":
                open_web_browser('http://timesofindia.indiatimes.com/')
                print '>>>', "Opeining 'Times of India' as per request...."
            else:
                print '>>>', "I am sorry , I am not updated with the latest data online... i will update my data and let you know."

        if person_in in info:
            print '>>>', "Sure {}, Give me a min....".format(person_name)
        
        if person_in in exit_code:
            print '>>>', 'Nice to talk to you ! Bye '
            break
        
if __name__ == "__main__":
    sys.exit(main())
