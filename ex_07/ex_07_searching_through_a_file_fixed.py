fhand = open('chat.txt')
for line in fhand:
#we only print the lines that start with '9/15/22, 15:'
    if line.startswith('9/15/22, 15:'):
        print(line)
