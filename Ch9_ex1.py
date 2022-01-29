fname = input('Enter the file name: ') #prompts user for file name to search
try:
    fhand = open(fname) #opens file
except:
    print('File cannot be opened:', fname) #returns 'File cannot be opened' to user and quits
    exit()
count = 0 #establishes line count at 0
counts = dict() #creates dictionary under variable counts
for line in fhand: #looks at user's chosen program line by line
    words = line.split()  #splits lines into words
    for word in words: #looks at line word by word
        count += 1
        if word in counts: #looks at words already in counts = dict()
            continue #discards duplicate words
        counts[word] = count #Value is first time word appears
if 'Python' in counts:
    print('True') #returns true if python is in counts = dict()
else:
    print('False') #returns false if python is in counts = dict()
