##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.office365.com)

import smtplib
import datetime as dt
import pandas as pd
import random


PLACEHOLDER = "[NAME]"
MY_EMAIL = "python100daytest@hotmail.com"
PASSWORD = "myymccmomgeapfmi" # App password


now = dt.datetime.now()
today = (now.month, now.day)


data = pd.read_csv("birthdays.csv")
birthdays_dict = {(row.month,row.day):row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        letter = contents.replace(PLACEHOLDER, birthdays_person['name'])

with smtplib.SMTP("smtp.office365.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL,password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=birthdays_person['email'],
        msg=f"Subject:Happy Birthday !\n\n{letter}"
    )
