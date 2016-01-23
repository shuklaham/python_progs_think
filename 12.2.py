
import random
def unstable_sort(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))

    t.sort(reverse = True)
    res = []
    for len,_,w in t:
        res.append(w)
    return w