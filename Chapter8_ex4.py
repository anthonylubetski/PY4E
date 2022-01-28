mylist = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split() #splits into words
    for word in words:
        if word in mylist: continue #discards duplicate words
        mylist.append(word) #updates the list
print(sorted(mylist)) #Alphabetizes that shit
