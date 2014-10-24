
frequency = {}
filename = '/Users/rhettshipp1/Desktop/Data-Files/random-data.txt'
with open(filename) as f:
    for line in f:
        words = line.split()
        for word in words:
            for item in word:
                if item not in frequency:
                    frequency[item] = 0
                frequency[item] += 1
print frequency

"""
alternatively, my if statement could have looked like:
if item in frequency:
    frequency[item] += 1
else:
    frequency[item] = 1
"""