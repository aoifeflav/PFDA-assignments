# The program should simulate 1000 individual battle rounds in Risk (3 vs 2) and plot the result.
# Author: Aoife Flavin

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



# Function to simulate armies of arbirary size fighting eachother
def simulate_war(attacker_size, defender_size, num_simulations):
    attacker_wins = 0
    defender_wins = 0
    
    for _ in range(num_simulations):
        # Army sizes for each simulation
        attacker_army = attacker_size
        defender_army = defender_size
        
        # keep going until one side is wiped out
        while attacker_army > 0 and defender_army > 0:
            attacker_loses, defender_loses = risk_game()
            attacker_army -= attacker_loses
            defender_army -= defender_loses
        
        # Check which side won
        if attacker_army > 0:
            attacker_wins += 1
        else:
            defender_wins += 1
    
    # Plotting the results using a pie chart
    categories = ['Attacker Wins', 'Defender Wins']
    values = [attacker_wins, defender_wins]

    plt.figure(figsize=(8, 8))
    colors = ['pink', 'purple']
    plt.pie(
        values,
        labels=categories,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
    )

    # title
    plt.title(f'Risk Full War Simulation ({num_simulations} Rounds)')

    # Display the pie chart
    plt.show()

# example
simulate_war(attacker_size=55, defender_size=67, num_simulations=500)


#Source: 
# https://thepythoncodingbook.com/2022/12/30/using-python-numpy-to-improve-board-game-strategy-risk/
# https://stackoverflow.com/questions/74421396/risk-game-with-python
# https://www.geeksforgeeks.org/random-numbers-in-python/
# https://realpython.com/python-zip-function/