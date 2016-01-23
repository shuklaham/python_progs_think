
def chop(l):
    del l[0]
    del l[len(l)-1]


orig_list_str = raw_input().split(" ")
chop(orig_list_str)
print orig_list_str