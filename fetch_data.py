import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from config import SHEET_NAME

def fetch_expenses():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).sheet1
    records = sheet.get_all_records()
    return pd.DataFrame(records)
