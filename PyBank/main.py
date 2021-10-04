import os
import csv
from datetime import datetime

#defining file path
filepath_read = os.path.join("Resources", "budget_data.csv")

months = []
changes = []
change = 0
profit_losses = []

#Defining function for statistical anaylsis
def financial_analysis(budgetdata):

    #The total number of months included in the dataset
    date = datetime.strptime(budgetdata[0],'%b-%Y')
    months.append(date.month)
    months_total = len(months)

    #The net total amount of "Profit/Losses" over the entire period
    profit_losses.append(float(budgetdata[1]))
    net = sum(profit_losses)

    #Average of the changes
    change = profit_losses - change
    changes.append(change)
    change = profit_losses
    
    #The average of the changes in "Profit/Losses" over the entire period
    total_change = sum(changes)
    average_change = total_change/len(changes)

    #The greatest increase in profits (date and amount) over the entire period
    gincrease_prof = changes.max()
    gincrease_date = budgetdata[0]
    
    #The greatest decrease in losses (date and amount) over the entire period
    gdecrease_loss = changes.min()
    gdecrease_date = budgetdata[0]

#opening and reading budget_data.csv input file
with open(filepath_read, 'r') as budgetdata_csv:
    csvreader = csv.reader(budgetdata_csv, delimiter = ',')
    csvheader = next(csvreader)

    for rows in csvreader: 
        financial_analysis(rows)

#prining results to the terminal window
print(f'Financial Analysis')
print('--------------------------------')
print(f'Total Months: {months_total}')
print(f'Total: {net}')
print(f'Averange change: {average_change}')
print(f'Greatest Increase in Profits: {gincrease_date} (${gincrease_prof})')
print(f'Greatest Decrease in Losses: {gdecrease_date} (${gdecrease_loss})')

#exporting results to the text file
filepath_write = os.path.join("Analysis", "output.csv")

with open(filepath_write, 'w', newline='') as txtfile:
    outputxt = csv.writer(txtfile, delimiter= '')
    #writing rows
    outputxt.writerow('Financial Analysis')
    outputxt.writerow('--------------------------------')
    outputxt.writerow('Total Months: {months_total}')
    outputxt.writerow('Total: {net}')
    outputxt.writerow('Averange change: {average_change}')
    outputxt.writerow('Greatest Increase in Profits: {gincrease_date} (${gincrease_prof})')
    outputxt.writerow('Greatest Decrease in Losses: {gdecrease_date} (${gdecrease_loss})')

    