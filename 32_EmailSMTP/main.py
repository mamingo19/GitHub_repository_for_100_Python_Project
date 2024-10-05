# import smtplib
#
# my_email = "anonymous2528201122@gmail.com"
# password = "yffpmpqogbpvxjer"
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr = my_email, to_addrs = "ndlanh22052002@gmail.com", msg="Subject:lan anh a`!\n\ntai sao lam ban cua nhau lau nhu v ma Lan Anh thay email cua tui Lan Anh lai khong rep??? tui buon lam biet ko?")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import smtplib
import datetime
import random

MY_EMAIL = "anonymous2528201122@gmail.com"
PASSWORD = "yffpmpqogbpvxjer"

now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL, to_addrs = "huytton119@gmail.com", msg=f"Subject:Quote!\n\n{quote}")


