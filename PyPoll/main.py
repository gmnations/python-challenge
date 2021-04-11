# imports
import os
import csv

#Set the path(having errors often with where this file lives in the path
election_data = os.path.join('Resources','election_data.csv')


# Declare variables
total_votes_cast = 0 # for holding total count of votes 
candidate_list = [] # has list of all candidates names
candidate_percentage = {}
current_candidate = "" # holds current candidates name
candidate_votes = {} # has key value pair of each candidate & their votes
most_votes = 0


#Open the CSV
with open(election_data, newline="") as csvfile:
    election_data_reader = csv.reader(csvfile, delimiter=",")

    #Skip the header row
    next(election_data_reader)

    #Loop through the CSV file
    for row in election_data_reader:
        
    # The total number of votes cast
        total_votes_cast += 1
        
    # The total number of votes each candidate won
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1

        else:
            candidate_votes[row[2]] = 1

for candidate in candidate_votes:

    candidate_percentage[candidate] = (candidate_votes[candidate]  /  total_votes_cast) *100

    if  candidate_votes[candidate] > most_votes:
        most_votes = candidate_votes[candidate]
        winner = candidate

        print(most_votes)
        print(total_votes_cast)

results_path = os.path.join('election_results.txt')

with open(results_path, 'w', newline="") as txtfile:

    txtfile.write(f'''
Election Results
-------------------------
Total Votes: {total_votes_cast}
-------------------------\n''')

    print(f'''\nElection Results
-------------------------
Total Votes: {total_votes_cast}
-------------------------''')

    for candidate, votes in candidate_votes.items():
        txtfile.write(f'{candidate}: {candidate_percentage[candidate]:.3f}% ({votes})\n')
        print(f'''{candidate}: {candidate_percentage[candidate]:.3f}% ({votes})''')
    
    txtfile.write(f'''-------------------------
Winner: {winner}
-------------------------''')

    print(f'''-------------------------
Winner: {winner}
-------------------------''')



