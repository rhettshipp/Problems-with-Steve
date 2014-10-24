line_count = 0
character_count = 0
word_count = 0

filename = '/Users/rhettshipp1/Desktop/Data-Files/Guest_list.txt'
with open(filename) as f:
    for line in f:
        words = line.split()        
        line_count += 1
        word_count += len(words)
        for word in words:
            character_count += len(word)
print line_count
print character_count
print word_count
