import os
import csv

#Set the path. I am having errors often with where this file lives in the path
budget_data = os.path.join('Resources','budget_data.csv')

num_rows = 0

for row in open('budget_data.csv'):
    num_rows += 1

print(num_rows)