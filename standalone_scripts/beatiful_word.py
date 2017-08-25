
def prime_num(n):
    if n>1:
        for i in range(2, n):
            if n%i == 0:
                return True
            else:
                False


n = input("Enter : ")
if prime_num(n):
    print "Not a Prime"
else:
    print "Prime Number"
