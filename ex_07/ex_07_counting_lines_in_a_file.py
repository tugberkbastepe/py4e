"""This is our file handle fhand

"""
fhand = open('chat.txt')
count = 0

# Now we count the number of lines in fhand
for line in fhand :
    count = count +1

# We print the # of lines counted
print('Line count: ', count)
