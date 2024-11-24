from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(PRACTICE_URL)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
print(price)

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

#---------------EMAIL-----------------------#

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} in on sale for {price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port = 587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr = os.environ["EMAIL_ADDRESS"],
            to_addrs= os.environ["EMAIL_ADDRESS"],
            msg = f"Subject: Amazon Price Alert!\n\n{message}\n{LIVE_URL}".encode("utf-8")
        )