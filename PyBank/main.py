#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 00:32:39 2024

@author: hannahkollmann
"""

# Importing required modules
import os
import csv

# Initializing variables for analysis
total_months = 0
net_total = 0
monthly_changes = []
dates = []

# Path to the CSV file
csv_path = os.path.join("//Users/hannahkollmann/Desktop/PyBank/Resources/budget_data.csv")

# Processing the CSV file
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header
    next(csvreader)

    # Read the first row to initialize variables
    first_row = next(csvreader)
    total_months = 1
    net_total = int(first_row[1])
    previous_amount = int(first_row[1])

    # Iterating over each row in the CSV
    for row in csvreader:
        # Tracking the total months and net total
        total_months += 1
        current_amount = int(row[1])
        net_total += current_amount

        # Calculating the monthly change and storing it
        change = current_amount - previous_amount
        monthly_changes.append(change)
        dates.append(row[0])

        # Updating the previous amount for the next iteration
        previous_amount = current_amount

# Calculating average change, greatest increase and decrease
average_change = round(sum(monthly_changes) / len(monthly_changes), 2)
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

# Dates of greatest increase and decrease
greatest_increase_date = dates[monthly_changes.index(greatest_increase)]
greatest_decrease_date = dates[monthly_changes.index(greatest_decrease)]

# Printing the financial analysis
print("Financial Analysis\n")
print("-------------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_total}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Writing the results to a text file
results_path = os.path.join("PyBank", "Analysis", "budget_analysis.txt")

with open(results_path, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-------------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
