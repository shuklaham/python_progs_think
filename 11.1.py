
def make_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        if line not in d:
            d[line] = 1
        else:
            d[line]+=1
    return d


word_dict = make_dict()

