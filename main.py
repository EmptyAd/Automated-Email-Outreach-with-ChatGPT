import pandas as pd
import pyautogui
import time
import subprocess
import pyperclip
import re
import os

# Load Configuration from Environment Variables
SPREADSHEET_URL = os.getenv("SPREADSHEET_URL", "YOUR_GOOGLE_SHEET_CSV_URL_HERE")
BROWSER_PATH = os.getenv("BROWSER_PATH", "/Applications/Opera.app/Contents/MacOS/Opera")
GMAIL_URL = os.getenv("GMAIL_URL", "https://mail.google.com/mail/u/0/")
CHATGPT_URL = "chat.openai.com"

USER_NAME = os.getenv("USER_NAME", "Your Name")
UNIVERSITY = os.getenv("UNIVERSITY", "Your University")
STUDY_YEAR = os.getenv("STUDY_YEAR", "Your Study Year")
CONTACT_NUMBER = os.getenv("CONTACT_NUMBER", "Your Contact Number")

# Load Google Sheets Data
df = pd.read_csv(SPREADSHEET_URL)
print(df)

# Open Browser (Only Once)
subprocess.Popen([BROWSER_PATH])
time.sleep(3)

# Open ChatGPT
pyautogui.typewrite(CHATGPT_URL, interval=0.1)
pyautogui.press("enter")
time.sleep(5)

# Open Gmail
pyautogui.hotkey("command", "t")
time.sleep(1)
pyautogui.typewrite(GMAIL_URL, interval=0.025)
pyautogui.press("enter")
time.sleep(5)

# Switch back to ChatGPT
pyautogui.hotkey("ctrl", "tab")
time.sleep(1)

for _, row in df.iterrows():
    email_id = row.get("Email", "").strip()
    company = row.get("Company", "").strip()
    role = row.get("Role", "").strip()

    if not email_id or not company or not role:
        print("Skipping incomplete entry.")
        continue

    # Generate Email Prompt
    prompt = f"""Write a concise, professional email to apply for the {role} position at {company}. I don’t know the Hiring Manager’s name, so address it generically. Keep the text plain, without bolding or formatting, as it will be copied directly. Do not add extra details beyond what is provided. Include the following details: - Name: {USER_NAME} - University: {UNIVERSITY}, {STUDY_YEAR} - Contact Number: {CONTACT_NUMBER} Ensure the email is polite, to the point, and clearly expresses my interest in the role."""

    pyautogui.typewrite(prompt, interval=0.025)
    pyautogui.press("enter")
    time.sleep(20)

    # Copy Generated Email
    pyautogui.moveTo(493, 635)  
    pyautogui.mouseDown()
    time.sleep(1)
    for _ in range(2):
        pyautogui.press("tab")
        time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(2)

    email_text = pyperclip.paste().strip()
    print("ChatGPT Response:", email_text)

    # Extract Subject & Body
    subject_match = re.search(r"Subject:\s*(.*)", email_text)
    subject = subject_match.group(1) if subject_match else "Job Application"
    body = re.sub(r"Subject:.*?\n\n", "", email_text, flags=re.DOTALL).strip()

    print("Subject:", subject)
    print("\nBody:\n", body)

    # Switch to Gmail
    pyautogui.hotkey("ctrl", "tab")
    time.sleep(1)

    # Compose New Email
    pyautogui.press("c")
    time.sleep(1)

    # Recipient Email
    pyautogui.typewrite(email_id, interval=0.025)
    pyautogui.press("enter")
    time.sleep(0.1)

    # Subject
    pyautogui.press("tab")
    pyautogui.typewrite(subject, interval=0.025)
    time.sleep(0.1)

    # Body
    pyautogui.press("tab")
    pyautogui.typewrite(body, interval=0.025)
    time.sleep(0.1)

    # Send Email (Uncomment to Enable)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(0.2)

    print(f"Email sent to: {email_id}")

    # Switch back to ChatGPT
    pyautogui.hotkey("ctrl", "tab")

print("Done")
