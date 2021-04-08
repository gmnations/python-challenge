#import modules
import os
import csv

#set path
budget_data = os.path.join('Resources','budget_data.csv')

#set output of txt file
txt_path = "output.txt"

#variables

#Now we can pull the headers from our csv file to use in our code and skip the header when looking at the column values
with open(pybank_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #We need to create an empty list for total_months, total_profits, monthly_change
    total_months = []
    total_profit = []
    monthly_change = []
    #Look inside the rows in our open csv
    for row in csvreader:
        #We need to add values within the rows from column 0 to our empty list for total_months
        total_months.append(str(row[0])













#   * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

#   * As an example, your analysis should look similar to the one below

