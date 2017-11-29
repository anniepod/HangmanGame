#first make list
import random
easywords = ["venezuela", "mythology", "frightful", "heartsick"]
#response = input(("Welcome to Hangman! Select a level of difficulty: easy , medium, or hard?"))
random.shuffle(easywords)
print(easywords)
targetword=easywords[0]
print(targetword)
print(" _ _ _ _ _ _ _ _ _ ")

    