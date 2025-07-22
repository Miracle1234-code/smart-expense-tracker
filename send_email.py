import smtplib
from email.mime.text import MIMEText
from config import SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL

def send_alert_email(total):
    subject = "🚨 Budget Alert"
    body = f"""
    Hi there,

    You spent ₦{total:,} in the last 7 days.

    Your budget limit was crossed. Please monitor your spending carefully.

    Regards,
    Smart Expense Tracker
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("📩 Email alert sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)
