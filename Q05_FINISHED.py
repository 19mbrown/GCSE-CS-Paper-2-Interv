# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
import random

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
numberList = []

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def generateList (inList, inCount):
    for count in range (inCount):
        randomNumber = random.randint (1, 100)
        inList.append (randomNumber)

# =====> Write your code here



# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
generateList (numberList, 100)
print (evenMean (numberList))
