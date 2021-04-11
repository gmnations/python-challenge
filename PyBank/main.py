#Import modules os and csv
import os
import csv

#Creating lists to store data
months = []
profit_loss_changes = []
previous_month = []
total_months = []
total_net = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


#Set path for the file ( had to change vscode settings in extensions/python and select "execute in this directory for the below to not error on finding the file")
budget_data = os.path.join('Resources','budget_data.csv')

#Open the CSV
with open(budget_data, newline="") as csvfile:

    budget_reader = csv.reader(csvfile, delimiter=",")
    next(budget_reader)

    for row in budget_reader:

        # Count of months
        count_months += 0
   
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss
        
        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            #profit_loss.append(float(row[1])
            profit_loss_changes.append(profit_loss_change)
            #profit_loss.append(float(row[1]))


            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss


#Calculate the total months included in the data set
total_months = (len(months))

#Calculate the net amount of Profit/Losses over the period of time
sum_profit_loss = sum(profit_loss_changes)
average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

#Calculate the average change per month
avg_change = sum_profit_loss / total_months

#Calculate the greatest increase in profits (date and amount)
max_profit = max(profit_loss_changes)

#Using the index of the greatest increase to find the date
index_max = profit_loss_changes.index(max_profit)
max_month = months[index_max]

#Calculate the greatest decrease in loss (date and amount)
min_profit = min(profit_loss_changes)

#Using the index of the greatest decrease to find the date
index_min = profit_loss_changes.index(min_profit)
min_month = months[index_min]

Joke_financial_analysis = (f'''--Super Financial Awesome Record--
----------------------------------
Total Months: {total_months}
Total: ${sum_profit_loss:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {max_month} {max_profit:.2f}
Greatest Decrease in Profits: {min_month} {min_profit:.2f}''')

#Print out analysis
print(Joke_financial_analysis)

#Create a .txt file containing the same analysis in the print out
analysis = open('super_awesome_moneymaking_financial_analysis.txt', 'w')

analysis.write(Joke_financial_analysis)

analysis.close()