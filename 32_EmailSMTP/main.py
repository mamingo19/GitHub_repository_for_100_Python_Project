import datetime
import pandas
import random
import smtplib

MY_EMAIL = "anonymous2528201122@gmail.com"
PASSWORD = "yffpmpqogbpvxjer"

today = (datetime.datetime.now().month, datetime.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        new_letter = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday Dear {birthday_person["name"]}!\n\n{new_letter}")
