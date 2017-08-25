# Eamples for the default dict

##from collections import defaultdict
##
##def default_val():
##    return "I am soooo cool"
##
##d = defaultdict(default_val, foo='bar')
##print d
##print d['foo']
##print d['bar']



# =====================================================

##l1 = [1,2,3,4,5,1,2,3,4,5,4,5,6,7,8,9,3,4,5,6,7]
##ul = []
##
####def uni(li):
####    for i in li:
####        if i not in ul:
####            ul.append(i)
####    return ul
####
####print uni(l1)
##
##[ul.append(i) for i in l1 if i not in ul]
##print ul

# =========================================================
from collections import deque
import threading
import time

candle = deque(xrange(21))

def handle(direction, options):
    while True:
        try:
            next = options()
        except IndexError :
            break

        else:
            print '%s is done and %d removed '%(direction, next)
            time.sleep(1.0)
    print '%s Done !'% direction
    return

left = threading.Thread(target=handle, args=('Left', candle.popleft))
right = threading.Thread(target=handle, args=('Right', candle.pop))

left.start()
right.start()


left.join()
right.join()


