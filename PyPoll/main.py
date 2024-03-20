#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 03:05:43 2024

@author: hannahkollmann
"""

# Importing necessary modules
import os
import csv

# Creating a path to the election data CSV file
csv_path = os.path.join("/Users/hannahkollmann/Desktop/PyPoll/Resources/election_data.csv")



# Initializing variables and lists for storing data
total_votes = 0
candidate_votes = {}
percentage_votes = []

# Processing the CSV file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skipping the header row

    # Looping through each row of the CSV file
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # Recording each candidate's vote count
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1

# Calculating vote percentages and identifying the winner
winner = max(candidate_votes, key=candidate_votes.get)
winner_votes = candidate_votes[winner]

for candidate, votes in candidate_votes.items():
    percentage = round((votes / total_votes) * 100, 3)
    percentage_votes.append(f"{candidate}: {percentage}% ({votes})")

# Printing election results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print('\n'.join(percentage_votes))
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

# Writing results to a text file
results_file = os.path.join("/Users/hannahkollmann/Desktop/PyPoll/Analysis/election_data.txt")
with open(results_file, "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("--------------------------\n")
    text_file.write('\n'.join(percentage_votes) + "\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("--------------------------\n")
