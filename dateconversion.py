size=int(input())
dates =[]
for i in range (size):
    dates.append(input())
#print(dates)
monthCode = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
modifiedDates =[]

for i in dates:
    DateMonthYear=i.split(' ')
    year=DateMonthYear[2]
    month=DateMonthYear[1]
    long_day=DateMonthYear[0]
    day=long_day[0:-2]
    if (len(day)==1):
        day='0'+ day
    modDate=year+'-'+monthCode[month]+'-'+day
    modifiedDates.append(modDate)

for i in range(len(modifiedDates)):
    print(modifiedDates[i])