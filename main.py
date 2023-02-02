import profit_loss, overheads, cash_on_hand

coh = cash_on_hand.cashOnHand()
print(coh)
overheads = overheads.overheads()
print(overheads)
pL = profit_loss.profitLoss()
print(pL)

f= open("summary_report.txt","w+")
#OVERHEADS
f.write(f'[HIGHEST OVERHEADS] {overheads[0]}: {overheads[1]}%' + '\n')
#COH
if len(coh) == 0:
    f.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY' + '\n')
else:
    for i in range(len(coh)):
        f.write(f'[CASH DEFICIT] DAY: {coh[i][0]}, AMOUNT: USD{coh[i][1]}' + '\n')
#PROFIT
if len(pL) == 0:
    f.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY' + '\n')
else:
    for i in range(len(pL)):
        f.write(f'[PROFIT DEFICIT] DAY: {pL[i][0]}, AMOUNT: USD{-1*pL[i][1]}' + '\n')


print('Done')
f.close()