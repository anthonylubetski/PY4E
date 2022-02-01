#Write a program that reads a file and prints the letters in decreasing order of frequency.
#Your program should convert all the input to lower case and only count the letters a-z.
#Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
#Find text samples from several different languages and see how letter frequency varies between languages.
#Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

alpha = 'abcdefghijklmnopqrstuvwxyz' #creates variable assigne dto alphabet
fname = input('Enter the file name: ') #prompts user for file name to search
try:
    fhand = open(fname, 'r') #opens file 'r' is for read only purposes
except:
    print('File cannot be opened:', fname) #returns 'File cannot be opened' to user and quits
    exit()
char = {}#creates dictionary for characters from document
text = fhand.read() #reads text in document
lwr = text.lower() #converts text to lowercase
for ch in lwr: #looks at characters in lowercase text
    if ch in alpha: #sees if characters are in alphabet variable
        char[ch] = char.get((ch), 0) + 1 #idiom for adding count of letters to dictionary
lst = list(char.items()) #creates list with itsm from tod dictionary
for key, val in sorted(char.items()): #sorts letters in descending order
    print(key, val) #prints letters and their count
