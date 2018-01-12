import random

easywords = ["scary", "plant", "money"]

random.shuffle(easywords)

#print(easywords)

targetword=easywords[0]

targetword = list(easywords[0])

print(targetword)

print("_ " * len(targetword))

#for letter in targetword:
#    print("_")


import turtle             
wn = turtle.Screen()      
alex = turtle.Turtle()


guessed = len(targetword) * "_ "
playing = True

while playing:
    guess = input("Guess a letter!")
    if targetword.__contains__(guess):
        print(guess)
        print("good job!")
        guessed = ((targetword.index(guess)) * "_ ") + guess + ("_ " * (4 - (targetword.index(guess))))
        print(guessed)
        
        if targetword == guessed
    else:
        alex.circle(50)
        print ("Wrong, guess again!" )



"""
if targetword.__contains__(guess):
    print(guess)
    print("good job!")
    guessed = ((targetword.index(guess)) * "_ ") + guess + ("_ " * (4 - (targetword.index(guess))))
    print(guessed)
else:
    alex.circle(50)
    print ("Wrong, guess again!" )



guess = input("Guess a letter!")
if targetword.__contains__(guess):
    print(guess)
    print("good job!")
    print(((targetword.index(guess)) * "_ ") + guess + ("_ " * (4 - (targetword.index(guess)))))
else:
    alex.right(90)
    alex.forward(100)
    
    
    
guess = input("Guess a letter!")
if targetword.__contains__(guess):
    print(guess)
    print("good job!")
    print(((targetword.index(guess)) * "_ ") + guess + ("_ " * (4 - (targetword.index(guess)))))
else:
    alex.right(45)
    alex.forward(50)


guess = input("Guess a letter!")
if targetword.__contains__(guess):
    print(guess)
    print("good job!")
    print(((targetword.index(guess) + 1) * "_ ") + guess + ("_ " * (4 - (targetword.index(guess)))))
else:
    alex.backward(50)
    alex.left(90)
    alex.forward(50)
    
    
    
guess = input("Guess a letter!")
if targetword.__contains__(guess):
    print(guess)
    print("good job!")
    print(((targetword.index(guess)) * "_ ") + guess + ("_ " * (4 - (targetword.index(guess)))))
else:
    alex.backward(50)
    alex.right(45)
    alex.backward(100)
    alex.right(90)
    alex.forward(50)
    
    
    
guess = input("Guess a letter!")
if targetword.__contains__(guess):
    print(guess)
    print("good job!")
    print(((targetword.index(guess)) * "_ ") + guess + ("_ " * (4 - (targetword.index(guess)))))
else:
    alex.backward(100)

guessword = input("What is the word? ")
if guessword == easywords[0]:
    print("You win!")
else:
    print("Sorry, You lost the game!")  """