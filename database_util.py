print("🚀 database_util.py is running!")  # ✅ Confirms execution starts
import csv  # ✅ This stays right after the debug statement

from datetime import datetime

csv_file = "signup_list.csv"  # ✅ Ensure correct file path

def append_to_csv(data):
    print("🔍 append_to_csv() was called with:", data)  # ✅ Confirms function execution

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # ✅ Generate timestamp
    new_entry = [data["name"], data["email"], data["phone"], timestamp]

    try:
        with open(csv_file, mode="a+", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            
            print(f"📝 Attempting to write {new_entry} to signup_list.csv...")  # ✅ Debug before writing
            writer.writerow(new_entry)  # ✅ Writing entry
            
            print(f"✅ Successfully wrote {new_entry} to signup_list.csv!")  # ✅ Debug after writing

    except Exception as e:
        print(f"⚠ CSV write failed: {e}")  # ✅ Catch errors
test_data = {
    "signup_date": "2025-06-02",
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "phone": "555-123-4567"
}

append_to_csv(test_data)  # ✅ Calls function after defining `test_data`

append_to_csv(test_data)  # ✅ Calls function directly