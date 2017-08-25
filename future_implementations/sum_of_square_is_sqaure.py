# sum of the square of the digits is equal to square


def simplification(m):
    summ = 0
    temp = m
    while temp>0:
        digits = temp % 10
        summ += digits**2
        temp = temp//10
    return summ

def squarevalue(n):
    sq = [i**2 for i in range(1, n+1)]
    print sq
    final = []
    for i in range(1, n+1):
        new = simplification(i)   
        if new in sq:
            final.append(i)
    print final
    print sum(final)
    

##n = input("input the value  : ")
squarevalue(23)
