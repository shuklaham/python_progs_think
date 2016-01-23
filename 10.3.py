

def cumulative(l):
    new_list = []
    prev_sum = 0
    for i in range(len(l)):
        val = prev_sum + int(l[i])
        new_list.append(val)
        prev_sum = val
        print str(new_list[i])+" ",

orig_list_str = raw_input().split(" ")

cumulative(orig_list_str)

