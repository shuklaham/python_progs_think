
def bin_search(l,w):
    if len(l) == 0:
        return False
    else:
        middle = len(l)/2
        if l[middle] == w:
            return True
        elif l[middle] > w:
            return bin_search(l[:middle],w)
        elif l[middle] < w:
            return bin_search(l[middle+1:],w)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print bin_search(testlist, 3)
print bin_search(testlist, 13)



