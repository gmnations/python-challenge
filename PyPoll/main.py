# imports
import os
import csv

#Set the path(having errors often with where this file lives in the path
csvpath = os.path.join('Resources','election_data.csv')


# Declare variables
totalVotes = 0 # for holding total count of votes 
currentCandidate = "" # holds current candidates name
candidateVotes = {} # has key value pair of each candidate & their votes
candidates = [] # has list of all candidates names
print(candidates)
