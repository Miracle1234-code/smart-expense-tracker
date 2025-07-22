from fetch_data import fetch_expenses
from analyze_data import check_spending
from send_email import send_alert_email

def main():
    print(" Fetching expenses...")
    df = fetch_expenses()

    print(" Checking spending...")
    total, over_budget = check_spending(df)

    print(f" Total spent in last 7 days: ₦{total:,}")
    if over_budget:
        print(" Budget exceeded. Sending alert email...")
        send_alert_email(total)
    else:
        print(" You’re within budget. No email needed.")

if __name__ == "__main__":
    main()
