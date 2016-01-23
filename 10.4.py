

def middle(l):
    new_list = []
    for i in range(len(l)):
        if i == 0 or i == (len(l)-1):
            continue;
        new_list.append(l[i])
    return new_list

orig_list_str = raw_input().split(" ")

print middle(orig_list_str)
