import os, os.path
import csv

list = os.listdir("../Resources")
number_files = len(list)

for numbers in range(number_files):
    eleccsv = os.path.join("election_data.csv")

    County= []
    Candidate = []
    Unique =[]
    CVoteCount = []
    CVotePercent =[]
    TotalCount = 0


    with open(eleccsv,'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None)

        for row in csvReader: 
            TotalCount = TotalCount + 1
            Candidate.append(row[2])
        for x in set(Candidate):
            Unique.append(x)
            cc = Candidate.count(x)
            CVoteCount.append(cc)
            CVotePercent.append(Candidate.count(x)/TotalCount)
        
        Winner = Unique[CVoteCount.index(max(CVoteCount))]



    with open('Election_Results_' + str(numbers+1) + '.txt', 'w') as text:
        text.write("Election Results for file 'election_data_"+str(numbers+1) + ".csv'"+"\n")
        text.write("----------------------------------------------------\n")
        text.write("Total Vote: " + str(TotalCount) + "\n")
        text.write("----------------------------------------------------\n")
        for i in range(len(set(Candidate))):
            text.write(Unique[i] + ": " + str(round(CVotePercent[i]*100,1)) +"% (" + str(CVoteCount[i]) + ")\n")
        text.write("----------------------------------------------------\n")
        text.write("Winner: " + Winner +"\n")
        text.write("----------------------------------------------------\n")