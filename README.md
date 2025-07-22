# 💸 Smart Expense Tracker

A simple, Python project that helps you track your expenses using **Google Sheets** and sends **email alerts** when your spending exceeds a certain limit.

This project is perfect for freelancers, students, or anyone who wants to keep their finances in check with automation!

---

# Features

- Stores expenses in **Google Sheets**
- Analyzes spending over the last 7 days
- Sends automatic **email alerts** if you overspend
- Keeps your credentials safe using `.env` files
- Easy to test and run in **Google Colab**

---

# Technologies Used

- Python 3
- Google Sheets API
- Gmail SMTP (for email alerts)
- Google Colab (for running it online)
- dotenv (.env file to hide sensitive info)

---

# How to Use This Project

# STEP 1: Set Up Google Sheets API

1. Go to [Google Developers Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the **Google Sheets API**
4. Create Service Account credentials
5. Download the JSON file → rename to `google_credentials.json`
6. Share your Google Sheet with the generated service email

---

# STEP 2: Prepare Your Google Sheet

1. Create a new Google Sheet
2. Name the sheet tab (e.g. `Expenses`)
3. Add this header row in the first row:
Date | Category | Description | Amount
4. Start adding sample data.

# STEP 3: Add Your `.env` File

Create a `.env` file with:
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SHEET_ID=your_google_sheet_id
BUDGET_LIMIT=20000


>  Tip: Use an App Password if you have 2FA on your Gmail.

---

# STEP 4: Run the App (Google Colab or Locally)

You can use `main.py` to run everything at once.

```bash
python main.py
It will:
Fetch the data
Analyze your last 7 days' expenses
Send you an alert if you’ve gone above your limit

Project Structure
smart-expense-tracker/
│
├── main.py                  # Entry point to run the full tracker
├── config.py                # Loads API keys and env vars
├── fetch_data.py            # Gets data from your Google Sheet
├── analyze_data.py          # Checks your spending patterns
├── send_email.py            # Sends alert if you overspent
├── sheet_utils.py           # Sheet helper functions
├── .env                     # Secret keys (not shared on GitHub)
├── README.md                # You're reading this!
├── google_credentials.json  # Google API credentials

Author
Built by Fatuade Miracle
