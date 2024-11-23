# The program should simulates 1000 individual battle rounds in Risk (3 vs 2) and plot the result.
#Author: Aoife Flavin

#import numpy and matplotlib modules
import numpy as np
import matplotlib.pyplot as plt

# Roll one dice
#def roll_dice():
#    return np.random.randint(1, 7)

#define the function for the game
def risk_game():
    attacker_roll = np.sort(np.random.randint(1,7, size = 3))[::-1] # attacker rolls 3 times
    defender_roll = np.sort(np.random.randint(1, 7, size=2))[::-1] # defender rolls 2 times
    #sort the rolls biggest to smallest

    #compare the dice
    attacker_loses = 0 #counter for each side's losses
    defender_loses = 0
    for a, d in zip(attacker_roll, defender_roll): 
        if a > d: #if attacker roll is higher than defender roll
            defender_loses += 1 #defender loses round
        else:
            attacker_loses += 1 #attacker loses round
    return attacker_loses, defender_loses

#1000 rounds
results = np.array([risk_game() for _ in range(1000)])

#total losses
total_attacker_losses = np.sum(results[:, 0])
total_defender_losses = np.sum(results[:, 1])

# plotting
categories = ['Attacker Losses', 'Defender Losses']
values = [total_attacker_losses, total_defender_losses]

# Plotting the results using a pie chart
plt.figure(figsize=(8, 8))
colors = ['pink', 'purple']
plt.pie(
    values,
    labels=categories,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
)

# Adding title
plt.title('Risk Battle Simulation (1000 Rounds)')

# Display the pie chart
plt.show()



#Source: 
# https://thepythoncodingbook.com/2022/12/30/using-python-numpy-to-improve-board-game-strategy-risk/
# https://realpython.com/python-zip-function/