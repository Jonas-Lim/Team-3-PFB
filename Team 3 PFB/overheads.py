# import Path from pathlib and csv module
from pathlib import Path
import csv

def overheads():
    """
    This function evaluates which overhead is the highest
    """
    highest = [[0, 0]]
    
    path = Path.cwd()/"Csv_reports"/"Overheads_day_90.csv" # the file path

    with path.open(mode = "r", encoding = "UTF-8", newline = "") as file: 
        reader = csv.reader(file) # create a reader object. reader variable is a list
        next(reader) # next() will return the next row. it skips the first row in this case

        for row in reader:
            if float(row[1]) > float(highest[0][1]): # finds the highest percentage under overheads
                highest[0] = row # finds the corresponding overhead expense to the highest percentage

    newpath = Path.cwd()/"Summary_report.txt" # creates a new text file path in the folder

    # opens the new path and appends the file
    with newpath.open(mode = "a", encoding = "UTF-8") as file:
        file.write(f"[HIGHEST OVERHEADS] {highest[0][0]}: {highest[0][1]}%\n") # writes a new line
overheads() # this calls the function
