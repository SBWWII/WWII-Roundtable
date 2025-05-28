import csv  # No indentation (0 spaces)

# Open the CSV file safely
import csv  # No indentation (0 spaces)

csv_file = "F:/GitHub/SBWWII/signup.csv"  # No indentation (0 spaces)

# Open the CSV file safely
with open(csv_file, mode="a", encoding="utf-8") as file:  # No indentation (0 spaces)
    reader = csv.reader(file)  # Indented exactly 4 spaces inside 'with open'

    for row in reader:  # Indented exactly 4 spaces inside 'reader'
        print(row)  # Indented exactly 4 spaces inside 'for row in reader'    reader = csv.reader(file)  # Indented exactly 4 spaces inside 'with open'


import csv

csv_file = "F:/GitHub/SBWWII/signup.csv"

# Open the file in append mode
with open(csv_file, mode="a", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    # Example row to append
    writer.writerow(["John", "Doe", "johndoe@example.com"])
