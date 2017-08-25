import sys

f = open(r"C:\Users\rkouravx\Desktop\alldata.txt", 'r')

check_list = ['q', 'exit', 'quit']
wordCollection = {}
for word in f.read().split():
    if word not in wordCollection:
        wordCollection[word] = 1
    else:
        wordCollection[word] += 1
# print wordcount
while True:
    n = raw_input('>>>')
    if n in check_list:
        sys.exit()
    if n in wordCollection:
        print n, ':', wordCollection[n]
