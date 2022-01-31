#This program counts the distribution of the hour of the day for each of the messages.
#You can pull the hour from the “From” line by finding the time string and then splitting
#that string into parts using the colon character.
#Once you have accumulated the counts for each hour, print out the counts,
#one per line, sorted by hour as shown below.
#python timeofday.py
#Enter a file name: mbox-short.txt
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1
fname = input('Enter the file name: ') #prompts user for file name to search
try:
    fhand = open(fname, 'r') #opens file 'r' is for read only purposes
except:
    print('File cannot be opened:', fname) #returns 'File cannot be opened' to user and quits
    exit()
count = 0 #establishes line count at 0
tod = dict() #creates dictionary under variable msgs
for line in fhand: #looks at user's chosen program line by line
    if line.startswith('From '): #looks for word from in each line
        time = line.split()[5]#prints second element on the
        hr = time.split(':')[0]
        tod[hr] = tod.get(hr, 0) + 1
lst = list(tod.items()) #creates list with itsm from tod dictionary
lst.sort() #sorts lst
for key, val in lst[:]:
    print(key, val) #prints time and how many emails at that time in order
