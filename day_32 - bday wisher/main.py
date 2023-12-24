import pandas as pd
import smtplib
import datetime as dt
import random



def send_email(to, message):
    my_email = "python.study@gmail.com"
    password = ""

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to, msg=message)

##################### Extra Hard Starting Project ######################

# TODO1. Update the birthdays.csv - DONE

# TODO2. Check if today matches a birthday in the birthdays.csv - DONE
today = dt.date.today()

# #1 - converting .csv in to list of dictionaries
bd_data = pd.read_csv("birthdays.csv")
bd_list =  bd_data.to_dict(orient="records")
to_send = []
letters_to_send = []

for item in bd_list:
    if item['day'] == today.day and item['month'] == today.month:
        to_send.append(item)

# TODO3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv - DONE

letter_path = f"letter_templates\letter_{random.randint(1,3)}.txt"

with open(letter_path) as file:
    letter = file.read()
    for item in to_send:
        dict_to_send = {
            "email" : item["email"],
            "letter" : letter.replace("[NAME]", item["name"]),
        }
        letters_to_send.append(dict_to_send)


# TODO4.  Send the letter generated in step 3 to that person's email address. - DONE
        
for item in letters_to_send:
    message = f"Subject:Happy Birdthday!!\n\n{item['letter']}"
    send_email(to=item["email"], message=message)
