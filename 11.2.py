
def histogram(s):
    d = dict()
    for c in s:
        val = d.get(c,0)
        d[c] = val+1
    return d


print histogram('brontosaurus')