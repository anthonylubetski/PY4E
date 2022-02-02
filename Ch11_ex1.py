#Write a simple program to simulate the operation of the grep command on Unix.
#Ask the user to enter a regular expression and count the number of lines that matched
#the regular expression:
import re
fname = input('Enter the file name: ') #prompts user for file name to search
try:
    fhand = open(fname, 'r') #opens file 'r' is for read only purposes
except:
    print('File cannot be opened:', fname) #returns 'File cannot be opened' to user and quits
    exit()
userinput = input('Enter regular expression: ')
for line in fhand:
    line = line.rstrip()
    if re.search(userinput, line):
        print(line)
