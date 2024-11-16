import yagmail
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(email_to=None, df=None):
    email_username = os.getenv('email_username')
    email_password = os.getenv('email_password')
    yag = yagmail.SMTP(email_username, email_password)

    filename = "data.xlsx"
    df.to_excel(filename, index=True)

    yag.send(
        to=email_to,
        subject='State Population Growth Data',
        contents='Cyclic Automation\nhttps://cyclic-automation.io',
        attachments=filename)