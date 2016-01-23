
import bisect

def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def bin_search(l,item):
    left = 0
    right = len(l) -1
    temp = l
    while len(temp)!=0:
        middle = (left+right)/2
        if l[middle] == item:
            return middle
        else:
            if l[middle] > item:
                right = middle -1
                temp = l[left:right+1]
            else:
                left = middle + 1
                temp = l[left:right+1]
    return -1

print bin_search([0, 1, 2, 8, 13, 17, 19, 32, 42,],3)
print bin_search([0, 1, 2, 8, 13, 17, 19, 32, 42,],13)

t = make_word_list1()
flag = []

for i in range(len(t)):
    flag.append(0)

for i in range(len(t)):
    if flag[i] ==0:
        word = t[i]
        rev_word = word[len(word)-1::-1]
        ind = bin_search(t,rev_word)
        if ind != -1:
            flag[i] = 1
            flag[ind] = 1
            print 'pairs :', i, ' ',ind


