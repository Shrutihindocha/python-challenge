import os
import csv
import datetime

#defining file path
filepath_read = os.path.join("Resources", "budget_data.csv")

months = []
net = 0
changes = []
change = 0

#Defining function for statistical anaylsis
def financial_analysis(budgetdata):

    #The total number of months included in the dataset
    date = datetime.strptime(budgetdata[0],'%b-%Y')
    month = datetime.strptime(date, '%b')
    months = months.append(month)
    months_total = len(months)

    #The net total amount of "Profit/Losses" over the entire period
    profit_losses = float(budgetdata[1])
    net =+ profit_losses

    #Average of the changes
    change = profit_losses - change
    changes = changes.append(change)
    change = profit_losses

    total_change = sum(changes)
    average_change = total_change/len(changes)

    if budgetdata[1] < 0:
        loss = budgetdata[1]
        losses =+ loss

        if profit_or_loss != 0:
            change = budgetdata[1] - profit_or_loss
            no_of_changes = no_of_changes + 1
            profit_or_loss = budgetdata[1]
            #The greatest decrease in losses (date and amount) over the entire period
            gdecrease_loss = 

            if budgetdata[1] - profit_or_loss < change:
                greatest_change = change

    

    #Profits
    elif budgetdata[1] > 0:
        profit = budgetdata[1]
        profits =+ profit 
        
    
    #The average of the changes in "Profit/Losses" over the entire period
    average_profit_or_loss = net/months_total

    #The greatest increase in profits (date and amount) over the entire period
    gincrease_prof = 
    
    
    #prining results to the terminal window
    print(f'Financial Analysis')
    print('--------------------------------')
    print(f'Total Months: {months_total}')
    print(f'Total: {net}')
    print(f'Averange change: {average_profit_or_loss}')
    print(f'Greatest Increase in Profits: {budgetdata[0]} (${gincrease_prof})')
    print(f'Greatest Decrease in Losses: {budgetdata[0]} (${gdecrease_loss})')

    #exporting results to the text file
    filepath_write = os.path.join("Analysis", "output.csv")

    with open(filepath_write, 'w', newline='') as txtfile:
        outputxt = csv.writer(txtfile, delimiter= '')
        #writing rows
        outputxt.writerow('Financial Analysis')
        outputxt.writerow('--------------------------------')
        outputxt.writerow('Total Months: {months_total}')
        outputxt.writerow('Total: {net}')
        outputxt.writerow('Averange change: {change}')
        outputxt.writerow('Greatest Increase in Profits: {budgetdata[0]} (${gincrease_prof})')
        outputxt.writerow('Greatest Decrease in Losses: {budgetdata[0]} (${gdecrease_loss})')

#opening and reading budget_data.csv input file
with open(filepath_read, 'r') as budgetdata_csv:
    csvreader = csv.reader(budgetdata_csv, delimiter = ',')
    csvheader = next(csvreader)

    for rows in csvreader: 
        financial_analysis(rows)

    

    