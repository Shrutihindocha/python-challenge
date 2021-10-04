import os
import csv
from datetime import datetime

#defining file path
filepath_read = os.path.join("Resources", "budget_data.csv")

months = []
changes = []
change = 0
profit_losses = []

#opening and reading budget_data.csv input file
with open(filepath_read, 'r') as budgetdata_csv:
    csvreader = csv.reader(budgetdata_csv, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader: 
    #The total number of months included in the dataset
        date = datetime.strptime(row[0],'%b-%Y')
        months.append(date.month)
        months_total = len(months)

        #The net total amount of "Profit/Losses" over the entire period
        profit_losses.append(float(row[1]))
        net = sum(profit_losses)

        #Average of the changes
        profit_loss = float(row[1])
        change = profit_loss - change
        changes.append(change)
        #The greatest increase in profits (date and amount) over the entire period
        gincrease_prof = max(changes)
        if change == max(changes):  
            gincrease_date = row[0]
        #The greatest decrease in losses (date and amount) over the entire period
        gdecrease_loss = min(changes)
        if change == min(changes):
            gdecrease_date = row[0]
        change = profit_loss
        
    #The average of the changes in "Profit/Losses" over the entire period
    del changes[0]
    total_change = sum(changes)
    average_change = total_change/len(changes)

        

#prining results to the terminal window
print(f'Financial Analysis')
print('--------------------------------')
print(f'Total Months: {months_total}')
print(f'Total: {net}')
print(f'Averange change: {round(average_change,2)}')
print(f'Greatest Increase in Profits: {gincrease_date} (${gincrease_prof})')
print(f'Greatest Decrease in Losses: {gdecrease_date} (${gdecrease_loss})')

#exporting results to the text file
filepath_write = os.path.join("Analysis", "output.txt")

with open(filepath_write, 'w') as txtfile:
    
    #writing rows
    txtfile.write(
    f"""
    Financial Analysis
    --------------------------------
    Total Months: {months_total}
    Total: {net}
    Averange change: {round(average_change,2)}
    Greatest Increase in Profits: {gincrease_date} (${gincrease_prof})
    Greatest Decrease in Losses: {gdecrease_date} (${gdecrease_loss})
    """
        )

    