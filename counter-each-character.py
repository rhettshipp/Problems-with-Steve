"""
Task - count the frequency of each character appearing in the document
1-create a list of all unique characters
2-create a function that will take each character in the text file
and count how many times it appears.
3-create a command that calls out each unique character and
reports the frequency of that number appearing
"""
total_characters = []
filename = '/Users/rhettshipp1/Desktop/Data-Files/random-data.txt'
with open(filename) as f:
    for line in f:
        for item in line:
            total_characters.append(item)    
unique_characters = list(set(total_characters))
print total_characters
print unique_characters

