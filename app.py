import csv
from database_util import append_to_csv  # ✅ Import correct function

csv_file = "signup.csv"  # ✅ Ensure correct file path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ Ensure CORS is imported

app = FastAPI()  # ✅ FastAPI instance created

# ✅ Add CORS middleware to allow GitHub Pages requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sbwwii.github.io", "http://localhost"],  # ✅ Allow GitHub Pages & local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Existing code continues here
@app.get("/")  # Example route (modify based on your existing script)
async def home():
    return {"message": "Welcome to my API"}

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