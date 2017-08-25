import time
import sys
import ctypes
import datetime

timings = '''
    Satrt time is : {0}
    {1}
'''


def timer():
    return time.time()

def timer_popup():
    srating_msg = ctypes.windll.user32.MessageBoxA
    return srating_msg(None, timings.format(timer(), datetime.datetime.time(datetime.datetime.now()), 'Timer', 0)


def main():
    try:
        timer_popup()
        while 1:
            start = timer()
            print start , "-->", datetime.datetime.time(datetime.datetime.now())
    except KeyboardInterrupt:
        end = time.time()
        print end , "-->", datetime.datetime.time(datetime.datetime.now())
        timer_popup()
    

if __name__ == '__main__':
    sys.exit(main())
    


