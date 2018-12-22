import random
import time


def printResult(myList): 
    for i in myList: 
        print(i, " ", end="")
    print("\n")

def charInList(myChar, myList):
    for character in myList:
        if character == myChar:
            return True
    return False

def whichIndex(myChar, myList):
    count = 0
    result = []
    for i in myList:
        if myChar == i:
            result.append((count))
        count = count + 1
    return result

def checkWin(myList):
    for i in myList:
        if i == "_":
            return False
    return True


while(True): 
    # read some random lines 
    # assuming words.txt contains a single word 
    # in each line
    # print("Welcome to my Hangman Game")
    # time.sleep(0.8)
    # print("loading.")
    # time.sleep(0.9)
    # print("loading..")
    # time.sleep(1)
    # print("loading...")

    with open('words.txt') as myFile:
        size=sum(1 for _ in myFile)
    #print("Your number of line is", size)
    # print("\n")
    myFile = open("words.txt", "r")
    myRandom = random.randint(1, size)
    #print(myRandom)
    for i in range(myRandom):
        hangman_word = myFile.readline()
    
    #print(hangman_word)
    hangman_word = hangman_word.replace("\n", "")
    word_length = len(hangman_word)
    result = []
    for i in range(word_length): 
        result.append('_')
    hangman_list = list(hangman_word)
    print(hangman_list)
    life = word_length //2

    time.sleep(2)
    print("So here is your secret word: ")


    while(life > 0):
        time.sleep(2)
        printResult(result) 
        print("Your life :", life)
        time.sleep(1)
        user_input = input("What character is your guess? ")
        print("\n")
        if(charInList(user_input, hangman_list)):
            print("That's Correct Buddy!")
            correctIndexChar = whichIndex(user_input, hangman_list)
            for i in correctIndexChar:
                #print(correctIndexChar)
                result[i] = user_input
            if(checkWin(result)):
                print("*******Congratulation Bro!******")
                printResult(result)
                break
        else:
            print("Sorry Bro, Try again")
            life = life - 1
            if(life == 0):
                print("Game over mate.... :(")
                print("the correct answer is", hangman_word)
        #print('\n')

    yes_no = input("Do you want to play again mate? ")
    if(yes_no == "yes"):
        continue
    else: 
        break


