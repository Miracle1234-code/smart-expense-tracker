import os
from dotenv import load_dotenv

load_dotenv()  # Loads your environment variables from .env file (if used)

# Google Sheet name
SHEET_NAME = "My Expenses"

# Budget limit (for the past 7 days)
BUDGET_LIMIT = 20000  # You can change this

# Email settings
SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")
RECEIVER_EMAIL = os.getenv("EMAIL_USER")  # You can change if you want to send to another person
