import csv  # No indentation (0 spaces)

csv_file = "F:/GitHub/SBWWII/signup.csv"  # No indentation (0 spaces)

# Open the CSV file safely
with open(csv_file, mode="r", encoding="utf-8") as file:  # No indentation (0 spaces)
    reader = csv.reader(file)  # Indented exactly 4 spaces inside 'with open'

    for row in reader:  # Indented exactly 4 spaces inside 'reader'
        print(row)  # Indented exactly 4 spaces inside 'for row in reader'