from datetime import datetime
import csv

with open('data_task4_old.txt', 'r') as file:
    dataObj = file.read().split('\n')

fullset = [el.split('\t') for el in dataObj[1:]]
tIdAvg=[]
price = 1
resSum = 0
timeDeadline = 20*60
for el in fullset[:10]:
    item=[]
    timeStarted = datetime.strptime(el[3], "%Y-%m-%d %H:%M:%S")
    timeFinished = datetime.strptime(el[4], "%Y-%m-%d %H:%M:%S")
    timedelta = timeFinished - timeStarted
    timeOnMicroTask = timedelta.total_seconds() / float(el[2])
    item.append(el[1])
    item.append(el[2])
    item.append(timeOnMicroTask)
    if (timeOnMicroTask < (20*60) and float(el[2]) > 1) or (timeOnMicroTask <= 60 and float(el[2]) == 1): 
        resSum = round((timeOnMicroTask / 30) * float(el[2]) * price, 2)
        item.append(resSum)
    else:
        resSum = round((timeOnMicroTask / 30) * float(el[2]) * price -(price*0.2), 2)
        item.append(resSum)

    tIdAvg.append(item)
print(tIdAvg)


