result = []
with open('/Users/rhettshipp1/Desktop/Data-Files/throwawaydata.txt') as f:
    for line in f:
        for i, char in enumerate(line):
            if i+1 > len(result):
                result.append({})
            if char in result[i]:
                result[i][char] += 1
            else:
                result[i][char] = 1
print result            
                