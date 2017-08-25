
def enterChars_inDigits(chars, digits):
    if len(chars) > 0:
        ring = str(digits)
        print chars.join([ring[i] for i in range(0, len(ring))])
    else:
        print "print enter chars properly, your chars size is 0"


char = raw_input("Enter you chars : ")
try:
    digit = input("Enter your Digit : ")
except:
    print "Only Digits are acceptable , Please try one more time !!"

enterChars_inDigits(char, digit)
