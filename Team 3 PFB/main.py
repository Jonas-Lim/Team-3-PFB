import profit_loss, overheads, cash_on_hand

coh = cash_on_hand.cashOnHand()
print(coh)
overheads = overheads.overheads()
print(overheads)
pL = profit_loss.profitLoss()
print(pL)

#------------- THIS IS TO ILLUSTRATE THE AUTOMATION OBJECTIVES AND EXPECTED OUTPUT IN A TEXT FILE --------- #
f= open("summary_report.txt","w+")

#------------ TO FIND OVERHEADS -------- #
# use f string
# find the highest overhead category
f.write(f'[HIGHEST OVERHEADS] {overheads[0]}: {overheads[1]}%' + '\n')

#------------ TO FIND COH ----------- #
# use if and else function 
# compute the difference of Cash-On-Hand if the current day is lower than the previous day
if len(coh) == 0:
    f.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY' + '\n')
else:
    for i in range(len(coh)):
        f.write(f'[CASH DEFICIT] DAY: {coh[i][0]}, AMOUNT: USD{coh[i][1]}' + '\n')

#--------- TO FIND THE PROFIT & LOSS -------- #
# compute the difference in the net profit column if net profit on the current day is lower than the previous day
if len(pL) == 0:
    f.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY' + '\n')
else:
    for i in range(len(pL)):
        f.write(f'[PROFIT DEFICIT] DAY: {pL[i][0]}, AMOUNT: USD{-1*pL[i][1]}' + '\n')

# print the variables 
print('Done')
f.close()
