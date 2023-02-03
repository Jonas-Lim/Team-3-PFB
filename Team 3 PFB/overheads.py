from pathlib import Path
from csv import reader

def overheads():
    with open('Overheads.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        category = []
        overheads = []
        for i in csv_reader:
            category.append(i[0])
            overheads.append(float(i[1]))

        highest = max(overheads)
        h = 0
        for k in range(len(overheads)):
            if overheads[k] == highest:
                h = k
        highestCat = [category[h], highest]

    return highestCat

            
