import os
import csv

#defining file path
filepath_read = os.path.join("Resources", "election_data.csv")

#opening and reading election_data.csv input file
with open(filepath_read, 'r') as electiondata_csv:
    csvreader = csv.reader(electiondata_csv, delimiter = ',')
    csvheader = next(csvreader)

    vote_count = []
    candidates = []
    candidate_votecounts = []
    percentages = []

    for row in csvreader: 
        vote_count.append(row[2])
        
    #A complete list of candidates who received votes
    candidates = set(vote_count)
    candidates_sorted = sorted(candidates, key = vote_count.count,reverse = True)
    # print(f'{candidates_sorted}')
    #The total number of votes cast
    total_votes = len(vote_count)
        
    print(f'Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------------')
    
    for candidate in candidates_sorted:
        candidate_votecount = vote_count.count(candidate)
        candidate_votecounts.append(candidate_votecount)

        percentage = round((candidate_votecount/total_votes)*100,3)
        percentages.append(percentage)

        print(f'{candidate}: {percentage}% ({candidate_votecount})')

        if candidate_votecount == max(candidate_votecounts):
            winner = candidate

    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    #exporting results to the text file
    filepath_write = os.path.join("Analysis", "output.txt")

    with open(filepath_write, 'w') as txtfile:
        
        #writing rows
        txtfile.write(
        f"""
        Election Results
        --------------------------------
        Total Votes: {total_votes}
        --------------------------------
        {for candidate in candidates_sorted:
            candidate_votecount = vote_count.count(candidate)
            candidate_votecounts.append(candidate_votecount)

            percentage = round((candidate_votecount/total_votes)*100,3)
            percentages.append(percentage)

            print(f'{candidate}: {percentage}% ({candidate_votecount})')

            if candidate_votecount == max(candidate_votecounts):
                winner = candidate}
        --------------------------------
        Winner: {winner}
        --------------------------------
        """
            )