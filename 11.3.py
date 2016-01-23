
def histogram(s):
    d = dict()
    for c in s:
        val = d.get(c,0)
        d[c] = val+1
    return d

def print_hist(h):
    l = h.keys()
    l.sort()
    for c in l:
        print c,h[c]

h = histogram('parrot')
print h
print_hist(h)