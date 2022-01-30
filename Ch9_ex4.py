#Add code to the above program to figure out who has the most messages in the file.
#After all the data has been read and the dictionary has been created,
#look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and print how many messages the person has.
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
        email_add[eaddy] = email_add.get(eaddy, 0) + 1 #counts number of email messages and adds to dictionary
mostemail = max(email_add, key=email_add.get) #variable mostemail assigned to max of who sent most emails
all_values = email_add.values() #variable all_values assigned to .values() method of gathering values from email_add dictionary
max_value = max(all_values) #finds max of all_values and assigns it to variable max_value
print(mostemail, max_value) #prints email of who sent most messages and how many messages they sent
