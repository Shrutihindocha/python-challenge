import os
import csv

#defining file path
filepath_read = os.path.join("Resources", "election_data.csv")

#opening and reading election_data.csv input file
with open(filepath_read, 'r') as electiondata_csv:
    csvreader = csv.reader(electiondata_csv, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader: 
        #The total number of votes cast

        #A complete list of candidates who received votes

        #The percentage of votes each candidate won

        #The total number of votes each candidate won

        #The winner of the election based on popular vote.

#prining results to the terminal window
print(f'Election Results')
print('--------------------------------')
print(f'Total Votes: {}')
print('--------------------------------')
print(f'{}: {} ({})')
print(f'{}: {} ({})')
print(f'{}: {} ({})')
print(f'{}: {} ({})')
print('--------------------------------')
print(f'Winner: {}')
print('--------------------------------')

#exporting results to the text file
filepath_write = os.path.join("Analysis", "output.txt")

with open(filepath_write, 'w') as txtfile:
    
    #writing rows
    txtfile.write(
    f"""
    Election Results
    --------------------------------
    Total Votes: {}
    --------------------------------
    {}: {} ({})
    {}: {} ({})
    {}: {} ({})
    {}: {} ({})
    --------------------------------
    Winner: {}
    --------------------------------
    """
        )