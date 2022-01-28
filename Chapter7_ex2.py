fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1 #counts number of lines with X-DSPAM
        colpos = line.find(':') #finds colon
        num = line[colpos+1:].strip() #removes all text except number
        spam = float(num)
        total = total + spam
average = total / count
print('Average spam confidence: ', average)
