

def histogram(s):
    d = dict()
    for c in s:
        val = d.get(c,0)
        d[c] = val+1
    return d

def inverse_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
        #inverse[val].append(temp)
    print inverse

hist = histogram('parrot')
print hist
inverse_dict(hist)