#Write a program to read through a mail log,
#build a histogram using a dictionary to count how many messages have
#come from each email address, and print the dictionary.
fname = input('Enter the file name: ') #prompts user for file name to search
try:
    fhand = open(fname, 'r') #opens file
except:
    print('File cannot be opened:', fname) #returns 'File cannot be opened' to user and quits
    exit()
count = 0 #establishes line count at 0
email_add = dict() #creates dictionary under variable msgs
for line in fhand: #looks at user's chosen program line by line
    if line.startswith('From '): #looks for word from in each line
        eaddy = line.split()[1]#prints second element on the
        email_add[eaddy] = email_add.get(eaddy, 0) + 1
print(email_add)
