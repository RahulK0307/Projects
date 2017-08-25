
import sys

step = []
for line in sys.stdin.readlines():
    step.append(line.rstrip())

def common_suffix(first, second):
    l1 = list(first)
    l2 = list(second)       
    match = []
    minimum = min(len(l1), len(l2))
    for i in range(minimum):
        if cmp(l1[i], l2[i]) == 0:
            match.append(l1[i])

    print "".join(match)
        

##fword = raw_input("Enter first word : ")
##sword = raw_input("Enter second word : ")

fword = step[0]
sword = step[1]

common_suffix(fword, sword)
