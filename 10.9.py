
def remove_duplicates(l):
    char_count = dict()
    #flag = False
    for char in l:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] +=1
     #       flag = True
    return char_count.keys()

print remove_duplicates([1, 1, 1, 1, 1, 1, 2, 3])
