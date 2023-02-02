from pathlib import Path
import csv
def overheads():
    highest = [[0, 0]]
    
    path = Path.cwd()/"Team 3 PFB"/"Csv_reports"/"Overheads_day_90.csv"

    with path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if float(row[1]) > float(highest[0][1]):
                highest[0] = row

    newpath = Path.cwd()/"Summary_report.txt"

    with newpath.open(mode = "a", encoding = "UTF-8") as file:
        file.write(f"[HIGHEST OVERHEADS] {highest[0][0]}: {highest[0][1]}%\n")
overheads()
