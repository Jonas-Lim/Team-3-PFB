# import Path from pathlib and csv module
from pathlib import Path
import csv

# locate the csv file by creating a file path
fp = Path.cwd()/"profits_and_loss.csv" # for simplicity, use cwd() - current working directory

# creates an empty list to store the profit differences
differences = []

def calculate_difference(profitdifference):
    """
    This function calculates the difference between the current day's profit and previous day's profit and outputs the value if current profit is less than previous profit
    """
    previous_profit=100000000000 # makes the previous profit a variable, and assumes day 39's profit to be higher
    
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file) # create a reader object. reader variable is a list
        next(reader) # next() will return the next row. it skips the first row in this case
        for row in reader:
            current_profit = int(row[4]) # current profit is the fourth row and converts it to an integer
            
            if current_profit < previous_profit:
                pd = previous_profit - current_profit
                
                profitdifference.append([row[0],pd]) # appends the difference between profits

            previous_profit = current_profit # when the equattion loops, it takes the next day's profit as the current profit
    profitdifference.remove(profitdifference[0]) # removes the first data, as we do not know the previous day's data
    return profitdifference # returns the profit difference

print(calculate_difference(differences)) # prints out the function
