# PFDA-assignments

This is the repository of Aoife Flavin. The purpose of this repoitory is to complete the Asignments given in the module Programming fo Data Analytics, in Semester 2 of the Higher Diploma in Data Analytics at ATU.

In each section I will detail my approach to solving the assigned tasks and cite the sources I used while problem-solving.

## Table of Contents
* [Assignment 1 - Setup](#assignment-1)
* [Assignment 2 - Weather](#assignemnt-2)
* [Assignment 3 - Pie Chart](#assignment-3)
* [Assignment 5 - Risk](#assignemnt-5)
* [Assignment 6 - Weather](#assignment-6)


<a id="assignment-1"></a>
## ***Assignment 1 Setup***
### Description:
The very first assignment was to create a repository for this module, and upload a link to it. I chose to use three seperate repositories for my assignments, labs and project.

<a id="assignment-2"></a>
## ***Assignment 2 Weather***
    Task 1: Commit something to your assignment repository this week (anything)

    Task 2: Create a jupyter notebook called assignment2-weather.ipynb that has a nice plot of the temperature over time ( "dryBulbTemperature_Celsius" ) using the weatherreadings1.csv file.

### Description:
To complete this task I first imported the pandas and matplotlib.pyplot libraries. I then opened and read the CSV file and used a for loop to print out a list of column names. I then loaded the dataset as a pandas dataframe and converted the reportEndDateTime into the datetime format.

To visualy represent this information I created a line plot of the temperature over the 24 hour period the data was collected in.

<details>
           <summary>Sources</summary>
           <p>

1. https://www.geeksforgeeks.org/get-column-names-from-csv-using-python/
2. https://realpython.com/python-csv/ 
3. https://saturncloud.io/blog/how-to-convert-strings-in-a-pandas-data-frame-to-a-date-data-type/#:~:text=The%20Pandas%20to_datetime()%20Function,-Pandas%20is%20a&text=The%20to_datetime()%20function%20is,%2FYYYY%20%2C%20and%20many%20others.
4. https://www.geeksforgeeks.org/line-plot-styles-in-matplotlib/
</p>
</details>

<a id="assignment-3"></a>
## ***Assignment 3 Pie Chart***
    Create a notebook called assignment03-pie.ipynb containing a nice pie chart of peoples email domains in the csv file provided which contains data on 1000 people.

### Description:
To complete this task I first imported the pandas and matplotlib.pyplot libraries and looked at the first few lines of data. I then created a new column with just the email domains by splitting the email domain strings at the '@' sign. The next step was to count the number of each domain presesnt in the data.

To visualy represent this information I created a pie chart of the disribution of email domains and found that:
- 32% use example.net
- 3.1% use example.org
- 33.9% use example.com

<details>
           <summary>Sources</summary>
           <p>

1. https://www.w3schools.com/python/ref_string_split.asp
2. https://www.w3schools.com/python/matplotlib_pie_charts.asp
</p>
</details>

<a id="assignment-5"></a>
## ***Assignment 5 Risk***
    Write a program that simulates 1000 individual battle rounds in Risk (3 attacker vs 2 defender) and plots the result. One battle round is one shake of the attacker and defender dice.

    A more complicated version simulates a full series of rounds for armies of arbitrary sizes, until one side is wiped out.

### Description:
To complete this task I first imported the Numpy and Matplotlib.pyplot modules. I then split the project into two parts:

1. **Simulating Individual Battle rounds**
For this part I first created a function called risk_game which simulates a single battle round where the attacker rolls three dice and the defender rolls two dice. The dice are compared, and losses are assigned based on which side has higher rolls.
I then had the program run 1000 individual battle rounds, tallying total losses for both attackers and defenders. Finally I created a pie chart displaying the proportion of total losses for attackers and defenders after 1000 rounds.

2. **Simulating a Full War**
For this part I created a function called 'simulate_war' which simulates multiple battles between armies of arbitrary sizes until one side is wiped out. It counts how many times each side wins across multiple simulations.
I demonstrate this with an example where an army of 55 attackers battles against 67 defenders over 500 simulations.
Finally I created a pie chart which shows the percentage of victories for attackers versus defenders across all simulations.

<details>
           <summary>Sources</summary>
           <p>
1. https://thepythoncodingbook.com/2022/12/30/using-python-numpy-to-improve-board-game-strategy-risk/
2. https://stackoverflow.com/questions/74421396/risk-game-with-python
3. https://www.geeksforgeeks.org/random-numbers-in-python/
4. https://realpython.com/python-zip-function/
</p>
</details>

<a id="assignment-6"></a>
## ***Assignment 6 Weather***
    Using the weathe data from Knock Airport plot:
    - The temperature
    - The mean temperature each day
    - The mean temperature for each month
    - The Windspeed (there is data missing from this column)
    - The rolling windspeed (say over 24 hours)
    - The max windspeed for each day
    - The monthly mean of the daily max windspeeds

### Description:
This Jupyter notebook processes and visualises meteorological data from a CSV file containing hourly weather observations from Know Airport. It uses Pandas for data manipulation and Matplotlib for plotting. Here is how I handled the data:

**1. Data Loading and Cleaning**
The program reads data from the CSV file and columns are renamed for better readability. Missing or invalid values in key columns (e.g., temperature, wind speed) are handled by converting them to NaN and dropping rows with missing data. The Date and Time (UTC) column is converted to the datetime format.

**2. Air Temperature Analysis**

<u>a. Plotting Air Temperature Over Time</u>
The program plots air temperature against time for the entire dataset (1996–2024) as a scatter plot.

<u>b. Mean Daily Air Temperature (2020–2024)</u>
I filtered data between 2020 and 2024 then grouped data by date and calculated the daily mean air temperature. Then I plotted the mean daily air temperature as a line graph.

<u>c. Mean Monthly Air Temperature (1996–2024)</u>
I grouped data by month-year periods and calculated the monthly mean air temperature. Then I plotted the monthly mean air temperature as a line graph.

**3. Wind Speed Analysis**

<u>a. Mean Monthly Wind Speed (2018–2024)</u>
I filtered data between 2018 and 2024 and grouped it by month-year periods and calculated the monthly mean wind speed. I then plotted the monthly mean wind speed as a line graph.

<u>b. Rolling Mean Wind Speed (January 21, 2024)</u>
I filtered the data for January 21, 2024 the calculated a rolling mean wind speed with a window size of 3 observations. Then I Plotted the rolling mean wind speed over time for that day.

<u>c. Maximum Daily Wind Speed (2023)</u>
I Filtered the data for 2023 and grouped it by date and calculated the maximum daily wind speed. Then I Plotted the maximum daily wind speed over time for 2023.

<u>d. Monthly Mean of Daily Maximum Wind Speeds (2023)</u>
I re-used the maximum daily wind speeds in 2023 calculated above to find monthly means.I then plotted the monthly mean of daily maximum wind speeds.

<details>
           <summary>Sources</summary>
           <p>
1. https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
2. https://www.geeksforgeeks.org/how-to-drop-one-or-multiple-columns-in-pandas-dataframe/ 
3. https://www.geeksforgeeks.org/python-pandas-to_numeric-method/
4. https://www.datacamp.com/tutorial/loc-vs-iloc 
5. https://realpython.com/pandas-settingwithcopywarning/
6. https://medium.com/@gfakhira9/to-period-909ee90ce6c1
7. https://www.statology.org/rolling-mean-pandas/
8. https://www.geeksforgeeks.org/select-row-with-maximum-and-minimum-value-in-pandas-dataframe/
9. https://realpython.com/pandas-groupby/
10. https://www.geeksforgeeks.org/python-strftime-function/
</p>
</details>

