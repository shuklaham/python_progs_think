
def sumall(*l):
    s = 0
    for i in range(len(l)):
        s = s + l[i]
    return s

print sumall(1,2,3)

