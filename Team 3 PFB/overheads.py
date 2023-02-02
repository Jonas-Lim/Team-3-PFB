# import path from pathlib and csv module
from pathlib import Path
import csv
def overheads():
    """The function eveluates what is the highest overhead expanse """
    highest = [[0, 0]]
    
    path = Path.cwd()/"Csv_reports"/"Overheads_day_90.csv"

    with path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader)
#Will compre the percentages in the second row and use the highest percentage. Program will find the corresponding overhead for the percentage
        for row in reader:
            if float(row[1]) > float(highest[0][1]):
                highest[0] = row
# creates a new text file in the path

    newpath = Path.cwd()/"Summary_report.txt"

    with newpath.open(mode = "a", encoding = "UTF-8") as file:
        file.write(f"[HIGHEST OVERHEADS] {highest[0][0]}: {highest[0][1]}%\n")
#This calls the function
overheads()