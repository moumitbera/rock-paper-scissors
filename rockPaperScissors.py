import art
import random
import os

continuePlaying = True
score = 0
computerScore = 0

selectionChoices = [art.rock, art.paper, art.scissors]

def checkPlayAgain():
    global continuePlaying
    userPlayAgain = input("Do you want to play again? Type yes or no\n").lower()
    if(userPlayAgain=="yes" or userPlayAgain == "y"):
        os.system("cls")
    else:
        continuePlaying = False
        print(f"You scored {score} point(s) while the computer scored {computerScore} point(s)")
        if(score>computerScore):
            print("You won!")
        elif(score == computerScore):
            print("We tied.")
        else:
            print("You lost!")

def computerWins():
    global computerScore
    print("You lose.")
    computerScore = computerScore + 1
    checkPlayAgain()

def youWin():
    global score
    print("You win")
    score = score + 1
    checkPlayAgain()


while continuePlaying:
    userSelection = int(input("Enter 1 for rock, 2 for paper, 3 for scissors\n"))
    userIndex = userSelection - 1
    computerSelection = random.randint(0,2)
    if (userIndex>2):
        print("Invalid input.")
        checkPlayAgain()
    else:
        print("You play: \n" +selectionChoices[userIndex])
        print("I play: \n"+selectionChoices[computerSelection])
        if(userIndex == 0):
            if(computerSelection==0):
                print("We tie.")
                checkPlayAgain()
            elif(computerSelection==1):
                computerWins()
            else:
                youWin()
        elif(userIndex==1):
            if(computerSelection==0):
                youWin()
            elif(computerSelection==1):
                print("We tie.")
                checkPlayAgain()
            else:
                computerWins()
        elif(userIndex==2):
            if(computerSelection==0):
                computerWins()
            elif(computerSelection==1):
                youWin()
            else:
                print("We tie.")
                checkPlayAgain()
        else: 
            print("invalid input.")