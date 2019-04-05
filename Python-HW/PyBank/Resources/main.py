
import os, os.path
import csv

list = os.listdir("../Resources")
number_files = len(list)


for numbers in range(number_files):
    budgetcsv = os.path.join("budget_data.csv")
    
    Count=0
    date = []
    month=[]
    year=[]
    revenue =[]
    revenueChange =[]
    TotalRev =0
    TotalRevChange = 0
    RevBeg=0
    
    
    with open(budgetcsv,'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')

        next(csvReader, None)
        
        for row in csvReader:        
            #Append data from the row
            Count = Count + 1
            date.append(row[0])
            TotalRev = TotalRev + int(row[1])
            RevEnd = int(row[1])
            RevChg = RevEnd - RevBeg
            TotalRevChange = TotalRevChange + RevChg
            revenueChange.append(RevChg)
            datesplit = row[0].split('-')
            month.append(str(datesplit[0]))
            year.append(datesplit[1][-2:])
            RevBeg = RevEnd
    
    AveRevChg = TotalRevChange / Count
    GreatIncrease = max(revenueChange)
    GreatDecrease = min(revenueChange)
    IncreaseDate = date[revenueChange.index(GreatIncrease)]
    DecreaseDate = date[revenueChange.index(GreatDecrease)]
    CountMon = len(set(date))
    
    with open('financial_analysis_report_' + str(numbers+1) + '.txt', 'w') as text:
        text.write("Financial Analysis for file 'budget_data_"+ str(numbers+1) + ".csv'"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("    Total Months: " + str(CountMon) + "\n")
        text.write("    Total Revenue: " + "$" + str(TotalRev) +"\n")
        text.write("    Average Revenue Change: " + '$' + str(int(AveRevChg)) +'\n')
        text.write("    Greatest Increase in Revenue: " + str(IncreaseDate) + " ($" + str(GreatIncrease) + ")\n")
        text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate) + " ($" + str(GreatDecrease) + ")\n\n")