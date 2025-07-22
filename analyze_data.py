import pandas as pd
from datetime import datetime, timedelta
from config import BUDGET_LIMIT

def check_spending(df):
    # Convert 'Date' column to actual dates
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter rows from the last 7 days
    last_week = datetime.now() - timedelta(days=7)
    recent_spending = df[df['Date'] >= last_week]

    # Calculate total amount spent
    total = recent_spending['Amount'].sum()

    # Check if total exceeds budget
    is_over = total > BUDGET_LIMIT
    return total, is_over
