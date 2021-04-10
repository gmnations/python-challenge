# imports
import os
import csv

#Set the path(having errors often with where this file lives in the path
csvpath = os.path.join('Resources','budget_data.csv')

#Set the variables
total_months = 0
total_pl = 0
average_changes = 0
best_month = []
worst_month = []
dates = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # read the header row and skip if header present
    csv_header = next(csvreader)
   
first_row = next(csvreader)
total_months += 1
total_pl += int(first_row[1])
value = int(first_row[1])
   

    # read each row of data after the header
for row in csvreader:
         dates.append(row[0])
          
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
    profits.append(change)
     value = int(row[1])
        
        #Total number of months
    total_months += 1

        #Total net amount of "Profit/Losses over entire period"
    total_pl = total_pl + int(row[1])
        print(row)


