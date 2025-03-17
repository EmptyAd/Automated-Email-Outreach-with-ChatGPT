# Email Automation Script

## Overview
This Python script automates the process of sending job application emails by:
- Extracting email IDs, company names, and job roles from a **Google Sheets** document.
- Using **ChatGPT** to generate personalized email content.
- Automatically composing and sending emails via **Gmail**.

## Features
✅ Fetches public Google Sheets data dynamically.
✅ Uses **ChatGPT** to generate job application emails.
✅ Automates email composition and sending via **Gmail**.
✅ Works with **Opera browser** (configurable).
✅ Configurable via **environment variables** (no hardcoded personal data).

## Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- Required dependencies:
  ```bash
  pip install pandas pyautogui pyperclip python-dotenv
  ```
- A **Google Sheet** (set to public access) with columns:
  - `Email` (Recipient's email address)
  - `Company` (Company name)
  - `Role` (Job position)
<img width="418" alt="Screenshot 2025-03-17 at 2 32 53 PM" src="https://github.com/user-attachments/assets/d8e6802b-83f9-4392-8664-300e7fd514bf" />

## Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/EmptyAd/Automated-Email-Outreach-with-ChatGPT.git
   cd Automated-Email-Outreach-with-ChatGPT
   ```

2. **Set Up Environment Variables**
   Create a `.env` file in the project directory and add the following details:
   ```ini
   SPREADSHEET_URL="https://your_public_google_sheet_url_here"
   BROWSER_PATH="/Applications/Opera.app/Contents/MacOS/Opera"  # Adjust for Windows/Linux
   GMAIL_URL="https://mail.google.com/mail/u/0/"
   USER_NAME="Your Name"
   UNIVERSITY="Your University"
   STUDY_YEAR="Your Study Year"
   CONTACT_NUMBER="Your Contact Number"
   ```

3. **Run the Script**
   ```bash
   python main.py
   ```

## How It Works
1. The script **fetches job application data** from Google Sheets.
2. It **opens Opera, ChatGPT, and Gmail** in the browser.
3. ChatGPT **generates an email** based on job details.
4. The script **copies the generated email** and pastes it into Gmail.
5. It **automatically sends the email** to the recipient.

## Notes
- Ensure that **Opera is installed** on your system, or update `BROWSER_PATH` to match your preferred browser.
- To **prevent accidental email sending**, the `pyautogui.press("enter")` line for sending emails is **commented out**. Uncomment it when ready.

## Contributing
Pull requests are welcome! Please ensure changes maintain code readability and modularity.

