
def make_dict(word):
    word_count = dict()
    for char in word:
        if char not in word_count:
            word_count[char] = 1
        else:
            word_count[char] +=1
    return word_count

def compare_dict(d1,d2):
    keys1 = d1.keys()
    keys1.sort()
    keys2 = d2.keys()
    keys2.sort()
    if not (keys1==keys2):
        return False
    else:
        for c in keys1:
            if d1[c] != d2[c]:
                return False
        return True

dict1 = make_dict('salting')
dict2 = make_dict('lasting')

print compare_dict(dict1,dict2)


