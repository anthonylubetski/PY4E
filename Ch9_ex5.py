fname = input('Enter the file name: ') #prompts user for file name to search
try:
    fhand = open(fname, 'r') #opens file
except:
    print('File cannot be opened:', fname) #returns 'File cannot be opened' to user and quits
    exit()
count = 0 #establishes line count at 0
domains = dict() #creates dictionary under variable msgs
for line in fhand: #looks at user's chosen program line by line
    if line.startswith('From '): #looks for word from in each line
        eaddy = line.split('@')[1]#prints second element which is the email address
        domain = eaddy.split()[0] #prints frist element which is the domain in split eaddy
        domains[domain] = domains.get(domain, 0) + 1
print(domains)
