# this scripts will pop up the message box for reminding me for the lunch time
# start and end time. This will work on the basis of system time.
# Acceptance criteria :-
# 1. It should pop up whenever we logged in into the system
# 2. it should map the starting time of my work
# 3. it should pop up whenever i will complete my 9 working hours including lunch
# 4. it should pop up when its a lunch time.


import os
import sys
import time
import getpass
import ctypes
import datetime


currentTime = time.strftime("%H : %M %p")
dayName = time.strftime("%A")

startTime = time.time()

morning = '''
    Hello !! {0}

    Good Morning  :)

    You singed in day '{1}' at {2}
'''

lunch = '''
    {0}  -- Sorry to disturb you

    it's {1}  Lunch Time  :)
'''

evening = '''
    Hello !!  "{0}" 

    Good Evening  :)

    It's {1} .
    
    Time to Go HOME....Horrahhhhhh  :)
'''

bye = '''
    Bye,  "{0}" 

    See you tomorrow :)
'''

def getUserName():
    try:
        username = os.environ.get('USERNAME')
    except:
        username = getpass.getuser()
    return username


def morning_reminder_popup():
    morning_msg = ctypes.windll.user32.MessageBoxA
    return morning_msg(None, morning.format(getUserName(), dayName, currentTime), 'Morning Reminder', 0)


def lunch_reminder_popup():
    lunch_msg = ctypes.windll.user32.MessageBoxA
    return lunch_msg(None, lunch.format(getUserName(), currentTime), 'Lunch Reminder', 0)


def work_time_completion_popup():
    evening_msg = ctypes.windll.user32.MessageBoxA
    return evening_msg(None, evening.format(getUserName(), currentTime), 'GoHome Reminder', 0)

def exit_called():
    lunch_msg = ctypes.windll.user32.MessageBoxA
    lunch_msg(None, bye.format(getUserName()), 'Bye', 0)
    sys.exit()

def main():
    while time.time() >= startTime:
        morning_reminder_popup()
        time.sleep(60*60*4)
        lunch_reminder_popup()
        time.sleep(60*60*4)
        work_time_completion_popup()
        time.sleep(10)
        exit_called()


if __name__ == '__main__':
    main()
