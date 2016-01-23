
def histogram(s):
    d = dict()
    for c in s:
        val = d.get(c,0)
        d[c] = val+1
    return d

def reverse_lookup(d, v):
    val_list = []
    for char in d:
        if d[char] ==v:
            val_list.append(char)
    print val_list

h = histogram('brontosaurus')
k = reverse_lookup(h, 2)