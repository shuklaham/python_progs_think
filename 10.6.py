
def is_sorted(l):
    flag = True
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            flag = False
    return flag

print is_sorted([1, 2, 2])
print is_sorted(['b','a'])