import asyncio
import csv
import os
from fastapi_mail import FastMail, MessageSchema
from email_config import conf  # Ensure email_config.py exists

# Define the CSV file path
csv_file = "C:/Users/Jakee/Documents/GitHub/SBWWII/signup_list.csv"

# Function to send email notification
async def send_email(name, email, phone):
    message = MessageSchema(
        subject="New Signup Notification",
        recipients=["sbwwiiroundtable@gmail.com"],
        body=f"New signup:\nName: {name}\nEmail: {email}\nPhone: {phone}",
        subtype="plain",
    )

    fm = FastMail(conf)
    await fm.send_message(message)

# Function to append new signup and trigger email
async def add_signup(name, email, phone):
    # Append data to the CSV file **(Single Instance)**
    with open(csv_file, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])

    print(f"✅ New data has been written to the CSV file for {name}!")

    # Send email notification
    await send_email(name, email, phone)

# **Run the function with test data**
if __name__ == "__main__":
    asyncio.run(add_signup("John Doe", "john@example.com", "9876543210"))