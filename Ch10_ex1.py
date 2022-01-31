#Revise a previous program as follows:
#Read and parse the “From” lines and pull out the addresses from the line.
#Count the number of messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary.
#Then sort the list in reverse order and print out the person who has the most commits.
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
lst = list() #creates list
for key, val in email_add.items():#places tuples made from dictionary values in list
    lst.append((val, key)) #switches key and val positions

lst.sort(reverse=True) #reverses list from most emails to least
for key, val in l[:1]: #finds first position in tuple
    print(val, key) #prints email with most messages
