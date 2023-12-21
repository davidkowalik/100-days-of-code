import smtplib
import datetime as dt
import random

def send_email(to, message):
    my_email = "@gmail.com"
    password = ""

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to, msg=message)
        connection.sendmail()

today = dt.datetime.now().weekday()

if today == 3:
    print("czwartek")

    random_quote = ""

    with open("quotes.txt") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    mssg = f"Subject:Czesc w czwartek\n\nHello,\n\nTodays quote:\n{random_quote}"

    send_email(to="@gmail.com", message=mssg)