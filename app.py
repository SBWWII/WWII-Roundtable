import csv
from database_util import append_to_csv  # ✅ Import correct function

csv_file = "signup.csv"  # ✅ Ensure correct file path

# ✅ Read and display existing CSV content
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ✅ Prints existing CSV rows correctly

# ✅ Append new data using `database_util.py`
new_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210"
}

append_to_csv(new_data)  # ✅ Calls function with duplicate prevention & timestamp