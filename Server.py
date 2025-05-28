from flask import Flask, request
import csv

app = Flask(__name__)

csv_file = "C:/Users/Jakee/Documents/GitHub/SBWWII/signup.csv"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json  # Get JSON data from the request
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    # Append the data to signup.csv
    with open(csv_file, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])

    return "✅ Data successfully added to signup.csv!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)