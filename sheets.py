# -*- coding: utf-8 -*-
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load Google Sheets API credentials
SERVICE_ACCOUNT_FILE = "credentials.json"  # Ensure this file is in your directory
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Initialize the Sheets API service
service = build("sheets", "v4", credentials=credentials)

# Define your spreadsheet ID and data range
SPREADSHEET_ID = "1JTkccWK_4W2peThX-Oyw0wlCUqDd7ZpejET5LPF2WeE"
RANGE_NAME = "'Form Responses 1'!A1:D10"  # Correct sheet name & range
print(f"Using Spreadsheet ID: {SPREADSHEET_ID}")
print(f"Using Range: {RANGE_NAME}")
# Function to fetch data from the spreadsheet
def get_sheet_data():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get("values", [])

    return values if values else [["No data found"]]

if __name__ == "__main__":
    data = get_sheet_data()
    for row in data:
        print(f"Timestamp: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")