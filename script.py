# Open the CSV file safely
import csv

csv_file = "C:/Users/Jakee/Documents/GitHub/SBWWII/signup.csv"

# First, read existing content
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)  # ✅ Only define this once
    for row in reader:
        print(row)  # ✅ Prints existing CSV rows correctly

# Now, append new data to the CSV file
with open(csv_file, mode="a", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["John Doe", "john@example.com", "9876543210"])  # ✅ Adds new row

print("✅ New data has been written to the CSV file!")# Append new data to the CSV file
with open(csv_file, mode="a", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["John Doe", "john@example.com", "9876543210"])  # Example entry

print("✅ New data has been written to the CSV file!")