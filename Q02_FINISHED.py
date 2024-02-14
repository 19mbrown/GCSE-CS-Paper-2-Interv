# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
import random
# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS == "SCISSORS"
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
choices = [ROCK, PAPER, SCISSORS]
computerChoice = ""
u = ""
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
computerChoice = choices[random.randint (0, 2)
u = input ("Rock, Paper, Scissors: ")
u = u.upper ()
if u == computerChoice:
    print ("We have a tie!")
elif u == ROCK:
    if computerChoice != PAPER:
        print ("You lose, " + computerChoice + " covers " + u)
    else:
        print ("You win, " + u + " smashes " + computerChoice)
elif u == PAPER:
    if computerChoice == SCISSORS:
        print ("You lose, " + computerChoice + " cuts " + u)
    else:
        print ("You win, " + u + " covers " + computerChoice)
elif u == SCISSORS:
    if computerChoice == SCISSORS:
        print ("You lose, " + computerChoice + " smashes " + u)
    else:
        print ("You win, " + u + " cuts " + computerChoice)
else:
    print("Invalid input")
