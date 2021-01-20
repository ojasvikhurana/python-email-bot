import pandas as pd
import smtplib

e = pd.read_excel("Email.xlsx") # path of excel file
emails = e['Email'].values  # column name which contains all the emails

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()   # start the server
server.login("<your email id>", "< your mail id password>")  #login to your email id
msg = "hello this is an email send by python script"   # content of email
subject = "This is the subject of email"    # subject of email
body = "Subject: {}\n\n{}".format(subject,msg)   

for email in emails:
    server.sendmail("<your email id>",email,body)  # for sending individual emails
server.quit()    #  quit server
