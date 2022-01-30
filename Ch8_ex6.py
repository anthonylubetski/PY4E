mylist = []
while True:
    num = 0.0
    usrnum = input('Enter a number:') #gets input from user
    if usrnum == 'done':
        break # if user enters 'done' program finishes
    try:
        num = float(usrnum) #converts user input to float
    except ValueError:
        print('Invalid input') #let's user know if they're n idiot
        quit()
    mylist.append(num) #adds float to mylist
print('Maximum: ', max(mylist)) #prints max of mylist after user enters numbers and hits done
print('Minimum: ', min(mylist)) #prints min of mylist after user enters numbers and hits done
