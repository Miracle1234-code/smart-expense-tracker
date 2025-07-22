import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta

# Authenticate with Google Sheets
def connect_to_sheet(sheet_name):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("google_credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet

# Add a new expense to the sheet
def add_expense(sheet, category, description, amount):
    today = datetime.today().strftime('%Y-%m-%d')
    row = [today, category, description, str(amount)]
    sheet.append_row(row)

# Get total of expenses from last 7 days
def get_expense_summary(sheet):
    records = sheet.get_all_records()
    one_week_ago = datetime.today() - timedelta(days=7)
    total = 0
    for record in records:
        try:
            record_date = datetime.strptime(record['Date'], "%Y-%m-%d")
            if record_date >= one_week_ago:
                total += float(record['Amount'])
        except:
            continue
    return total
