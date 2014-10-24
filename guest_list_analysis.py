unique_guest = set()
filename = '/Users/rhettshipp1/Desktop/Data-Files/Guest_list.txt'
with open(filename) as f:
    f.next()
    for line in f:
        unique_guest.add(line.strip())
print unique_guest
print len(unique_guest)

"""
Steve's comments - 
Some changes to make - 

"""