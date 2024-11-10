# The program should simulates 1000 individual battle rounds in Risk (3 vs 2) and plot the result.
#Author: Aoife Flavin

#import numy module
import numpy as np

# Roll one dice
def roll_dice():
    return np.random.randint(1, 7)

print(roll_dice())







#Source: 
# https://thepythoncodingbook.com/2022/12/30/using-python-numpy-to-improve-board-game-strategy-risk/