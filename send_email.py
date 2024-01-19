import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Temp User"
email["to"] = "<insert to address here>"
email["subject"] = "Test email"

email.set_content(html.substitute({"name": "Gary"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("<insert your gmail id here>", "<insert your gmail app password here>")
    smtp.send_message(email)
    print("Success!")
