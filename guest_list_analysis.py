guest_list = []
filename = '/Users/rhettshipp1/Desktop/Data-Files/Guest_list.txt'
with open(filename) as f:
    f.next()    
    for line in f:
        guest_list.append(line)
unique_guest_list = list(set(guest_list))
print guest_list
print unique_guest_list
print len(unique_guest_list)