# if entered digit is 1234567 then it should not enter the * and - in between
# adjacent numbers should ne odd or even.
# if number is odd then enter * otheriwse -.

##def digit_manipulation(digit):
##    values = list(str(digit))
##    
##    final = []
##    for i in range(0, len(values) - 1):
##        m = int(values[i])
##        n = int(values[i+1])
##
##        if m == 0 or m == 1:
##            final.append(m)
##        elif m > 1:
##            if m % 2 == 0:
##                final.append(m)
##            elif m%2 == 0 and n %2 == 0:
##                m = m , '-' , n
##                final.append(m)
##            elif m%2 != 0:
##                final.append(m)
##            elif m%2 != 0 and n%2 !=0:
##                m = m, '*', n
##                final.append(m)
##
##    
##    print "Final Output : ", ''.join([str(i) for i in final])
##    
##
##d = input("Enter your digit : ")
##
##digit_manipulation(d)


def digit_manipulation(digit):
    values = list(str(digit))
    changed = []
    call = lambda 
    final = []
    for i in range(len(values)):
        if values[i] == 0 or values[i] == 1:
            final.append(values[i])
        elif int(values[i]) % 2 == 0:
            values[i] = values[i] + '-'
            final.append(values[i])
        else:
            values[i] = values[i] + '*'
            final.append(values[i])


    print "Final Output : ", ''.join(final)
    

d = input("Enter your digit : ")

digit_manipulation(d)
