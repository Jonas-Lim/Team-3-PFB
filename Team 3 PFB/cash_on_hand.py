from pathlib import Path
from csv import reader

def cashOnHand():
    with open('cash-on-hand-usd.csv', 'r') as read_obj:
        dict_test = {}
        csv_reader = reader(read_obj)
        header = next(csv_reader)

        for i in csv_reader:
            dict_test[int(i[0])] = int(i[1])

        dict_key = list(dict_test.keys())
        cash_def = []
        for i in range(1,len(dict_key)):
            day1 = dict_key[i] #41
            cash_day1 = dict_test[day1]
            day0 = day1-1
            cash_day0 = dict_test[day0]
            diff = int(cash_day1)-int(cash_day0)
            if diff < 0:
                cash_def.append([day1,diff])
    return cash_def  



        




