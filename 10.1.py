def simple_add(p):
    print p
    s = 0
    for j in range(len(p)):
        print p[j]
        s += int(p[j])
        return s


def nested_add(l):
    t = 0
    for i in range(len(l)):
        print l[i]
        t += simple_add(l[i])
        return t


print ('Gimme nested list');
inp = [[1, 2], [1, 1]]
# inp = raw_input()
print nested_add(inp)
