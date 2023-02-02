# import Path from pathlib and csv file
from pathlib import Path
import csv

# create a file to csv file
fp = Path.cwd()/"business-intelligence.csv"

# create an empty list to store values
differences = []


def calculate_difference(cash_on_hand_difference) :
    """
    Function will calculate difference between current cash on hand and previous cash on hand
    and output the values if the previous day value is higher than current day value
    """
    # create a variable of day 39's cash on hand 
    previous_cash_on_hand = 100000000000
    
    with fp.open(mode="r", encoding="UTF-8", newline="") as file :
        reader = csv.reader(file) # create a reader object
        next(reader) # the next() function will skip the first row and return next row
        for row in reader :
            current_cash_on_hand = int(row[1]) # current cash on hand is 1st row and convert it into an integer
            
            if current_cash_on_hand < previous_cash_on_hand :
                cd = previous_cash_on_hand - current_cash_on_hand
                
                cash_on_hand_difference.append([row[0],cd]) # append the difference between cash on hand

            previous_cash_on_hand = current_cash_on_hand # takes next day's cash on hand as current cash on hand
    cash_on_hand_difference.remove(cash_on_hand_difference[0]) # removes day 39's data as it is unknown
    return cash_on_hand_difference # return the cash on hand difference

print(calculate_difference(differences)) # print and execute function
