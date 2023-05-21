"""
We find the # of characters in our text file
"""

fhand = open('chat.txt')

# We read the whole file(newlines and all) into a single string
inp = fhand.read()
# We find the # of characters
print(len(inp))
# We print the first 20 character of the text file
print(inp[:20])
