def mycount (letter, word):
    num = 0
    for x in word:
        if x == letter:
            num = num +1
    return num
fruit= "banana"
letter2 = "a"
numa = fruit.count(letter2) #here is the counting invocation
print(str(numa))

word = input('Give me a word: ')
letter = input('Give me a letter: ')
numb = mycount (letter, word)
print ("There are " + str(numb) + " " + letter +  "'s in your word " + word)
