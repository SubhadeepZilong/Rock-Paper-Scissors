# ------------- Packages ---------------


import string
import random


# --------- Global Variables -----------


s=["Rock" , "Paper" , "Scissors"]
a=1


# --------- Functions -----------


# Randomising the choice
def display():
    return("".join(random.sample(s,1)))


# Displaying who won or if it was a tie
def check_result():
    ch=display()
    print("Computer has chosen: ",ch)
    if((ch=="Rock"and a==1)or(ch=="Paper"and a==2)or(ch=="Scissors"and a==3)):
        print("It was a draw.\n\n\n")
    elif((ch=="Rock"and a==2)or(ch=="Paper"and a==3)or(ch=="Scissors"and a==1)):
        print("Player has won.\n\n\n")
    elif((ch=="Rock"and a==3)or(ch=="Paper"and a==1)or(ch=="Scissors"and a==2)):
        print("Computer has won.\n\n\n")
    

# main funtion
def main():
    # Set global variables
    global a
    # Runnning a round of games
    while(a>0 and a<=3):
        # Each round
        print("Enter 1 for Rock")
        print("Enter 2 for Paper")
        print("Enter 3 for Scissors")
        print("Enter anything else to quit\n")
        a = int(input("Choose: "))
        if(a<=0 or a>3):
            break
        # Checking results
        check_result()
    # When player quits playing
    print("Thank you for playing.")


# ------------ Start Execution -------------


# Play a game of rock paper scissors
main()
    