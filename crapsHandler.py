#Eli Stewart
#9/29/23
#Creating the dice game known as Craps

import random as r


#This function defines the roll dice function that rolls the two dice
def rollDice():
  dice1 = r.randint(1,6)
  dice2 = r.randint(1,6)
  return dice1, dice2


#This function defines the first roll in the game
def rollHandler(dice1, dice2, point):
  if point > 1:
    return ifPoint(dice1, dice2, point)
  else:
    return firstRoll(dice1, dice2)
  
def firstRoll(dice1, dice2):
  sum = dice1 + dice2
  #These if, elif, else statemnts use sum to determine outcome of first roll
  if sum == 2:
    return 0
  elif sum == 3:
    return 0
  elif sum == 12:
    return 0
  elif sum == 7:
    return 1
  elif sum == 11:
    return 1
  else:
    return sum


#This function defines the scenario for when a point is established
def ifPoint(dice1, dice2, point):
  sum = dice1 + dice2
  if (sum == point):
    return 1
  elif (sum == 7):
    return 0
  else:
    return point


"""Looping the entire game 10,000 times
for i in range(10000):
  main()
print("You won {} games of 10,000".format(numOfWins))"""