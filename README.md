# 💰 Smart Expense Tracker with Email Alerts

Track your weekly expenses using Google Sheets + Python.  
If you overspend, you'll receive an email warning!

---

## 🔧 Features:
- Reads your expenses from a Google Sheet
- Checks if spending in the last 7 days crossed your budget
- Sends email alerts automatically

---

## 📦 Tech Stack:
- Python
- Google Sheets API
- Gmail SMTP
- Pandas

---

## 📄 How to Use:

1. Create a Google Sheet called `My Expenses` with columns:
   - Date | Item | Amount | Category

2. Enable:
   - Google Sheets API
   - Google Drive API

3. Create a service account and download `google_credentials.json`

4. Share your Google Sheet with the service account email

5. Set up `.env` like this:

```env
EMAIL_USER=youremail@gmail.com
EMAIL_PASS=your_app_password  # use App Password, not your main password
