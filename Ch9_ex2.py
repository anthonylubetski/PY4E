#Write a program that categorizes each mail message by which day of the week the commit was done.
#To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the week.
#At the end of the program print out the contents of your dictionary (order does not matter).
fname = input('Enter the file name: ') #prompts user for file name to search
try:
    fhand = open(fname, 'r') #opens file
except:
    print('File cannot be opened:', fname) #returns 'File cannot be opened' to user and quits
    exit()
count = 0 #establishes line count at 0
days = dict() #creates dictionary under variable dow
for line in fhand: #looks at user's chosen program line by line
    if line.startswith('From '): #looks for word from in each line
        day = line.split()[2]#prints third element on the
        days[day] = days.get(day, 0) + 1 
print(days)
