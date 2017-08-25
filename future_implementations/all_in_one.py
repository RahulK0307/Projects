# number should be prime number if it is not dividing by the other numbers


def find_prime(n):
    for i in range(2, n):
        if n%i == 0:
            break
    else:
        return True


def factorial(n):
    factorial = 1
    if n < 0:
        print "Factorial for {} does not exits - it is a negative number.".format(n)
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            factorial = factorial * i
        print factorial


def recur_factorial(n):
    if n < 0:
        print "Factorial for {} does not exits - it is a negative number.".format(n)
    elif n == 1:
        return n
    else:
        return n * recur_factorial(n-1)
        

def factors(n):
    fact = []
    for i in range(1, n+1):
        if n % i == 0:
            fact.append(i)
    return fact

def find_armstrong(n):
    temp = n
    s = 0
    while temp > 0:
        digit = temp % 10
        s = s + digit**3
        temp = temp // 10
        
    if n == s:
        print " {} is an armstrong number ".format(n)
    else:
        print " {} is not an armstrong number ".format(n)
    

if __name__ == "__main__":
    print """
    which function you wants run :
        1 - Find prime Number
        2 - Find factorial
        3 - Recursive factorial
        4 - Factors of a number
        5 - Armstrong Number
        6 - Still thinking to implement

    """
    choice = input()
    if choice == 1:
        n = input("enter ur number  : ")
        if find_prime(n):
            print "Prime Number"
        else:
            print "Not a prime"

    elif choice == 2:
        n = input("enter ur number  : ")
        factorial(n)
        
    elif choice == 3:
        n = input("enter ur number  : ")
        print "Factorial is  :  ", recur_factorial(n)

    elif choice == 4:
        n = input("enter ur number  : ")
        print "Factors are  :   \n", factors(n)

    elif choice == 5:
        n = input("enter ur number  : ")
        find_armstrong(n)
        
    else:
        print "please enter your choice one more time from the given options."
