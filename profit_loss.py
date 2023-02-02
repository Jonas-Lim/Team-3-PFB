from pathlib import Path
from csv import reader

def profitLoss():
    with open('profit-and-loss-usd.csv', 'r') as read_obj:
        dict_test = {}
        csv_reader = reader(read_obj)
        header = next(csv_reader)

        for i in csv_reader:
            dict_test[int(i[0])] = i[1::]
        # print(dict_test)

        dict_key = list(dict_test.keys())
        deficit = []
        for i in range(1,len(dict_key)):
            day1 = int(dict_key[i])
            for k,v in dict_test.items():
                if k == day1:
                    profit_day1 = v[3]
            day0 = day1-1
            for k,v in dict_test.items():
                if k == day0:
                    profit_day0 = v[3]
            diff = int(profit_day1)-int(profit_day0)
            if diff < 0:
                deficit.append([day1,diff])
    return deficit  


        




