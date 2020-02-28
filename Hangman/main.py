import random
import time
import sys

def get_word():
    words = ["apple", "sandwitch", "chance", "winner", "chicken", "dinner"]
    return random.choice(words)
    
def check_character(character, word, newWord):
    word = list(word)
    temp = list(newWord)
    flag = False
    for i in range(len(word)):
        if word[i] == character:
            temp[i] = character
            flag = True
        elif str(word[i]).isalpha() == True:
            pass
        else:
            temp[i] = '*'
    newWord = ''.join(temp)
    return [newWord, flag]        
    
    
def play(name):
    chances = 3
    points = 0
    loop = True
    print("Welcome {} you have {} chances and your points are {}. ".format(name, chances, points))

    while loop:
        
        word = get_word()
        print("Word is : {}".format(len(word)* '*'))
        newWord = len(word) * '*'
        
        while chances != 0:
            if '*' in newWord:
                character = input("Enter a character: ")
                temp = check_character(character, word, newWord)
                newWord, flag = temp[0], temp[1]
                if chances == 0:
                    print("Guess was wrong. No remaining chances .")
                    print("Your score was: {}".format(points))
                    sys.exit(0)
                elif flag == False and chances != 0:
                    chances = chances - 1
                    print("Guess was wrong. Chances remaining are {}".format(chances))
                else:
                    print("Word is : {}".format(newWord))
            else:
                print("Hurray!!! you have guessed the word correctly.")
                points = points + 1
                print("Your points: {}".format(points))
                print("Your remaining chances: {} ".format(chances))
                loop = input("Would you like to continue(True/False only):")
                break


print("Welcome to the Hangman Game!!!! ")
time.sleep(1)
print("Loading.", end= "")
time.sleep(1)
print(".", end= "")
time.sleep(1)
print(".", end= "")
time.sleep(1)
print(".")

name = input("Enter your Name: ")
play(name)

