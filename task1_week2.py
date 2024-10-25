#Looking at a cereal dataset
#Author: Aoife Flavin

#Assignment 2 Weather
#Task 1: Commit something to your assignment repository this week (anything)

#import libaries
#Data Frames
import pandas as pd

#numpy
import numpy as np

#plotting
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("cereal.csv")

#take a look
#print(df.head())

# Create a bar chart showing how many of each cereal there are
#count how many of each cereal there are
brand_amount = df['name'].value_counts()

#put it in a bar chart
plt.figure(figsize=(10, 6)) 
brand_amount.plot(kind = 'bar', color = ['#e39ff6', '#2c041c', '#710193'], edgecolor='black')
plt.ylabel("Amount") 
plt.xlabel("Cereal")
plt.title("Amount of each Cereal")

plt.ylim(0, brand_amount.max() + 5)

plt.gca().spines['top'].set_visible(False) #remove line a top
plt.gca().spines['right'].set_visible(False) # remove line on right

plt.show()

print("There are an equal number of each cereal in this dataset")



# Sources:
# - https://www.kaggle.com/datasets/crawford/80-cereals?resource=download
# My pands projct from last year