import pandas as pd
import smtplib

e = pd.read_excel("Email.xlsx")
emails = e['Email'].values

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("<your email id>", "< your mail id password>")
msg = "hello this is an email send by python script"
subject = "This is the subject of email"
body = "Subject: {}\n\n{}".format(subject,msg)

for email in emails:
    server.sendmail("<your email id>",email,body)
server.quit()
