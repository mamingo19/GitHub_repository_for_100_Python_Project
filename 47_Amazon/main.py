from bs4 import BeautifulSoup
import requests
import smtplib

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

    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        result = connection.login("huytton119@gmail.com", "syds himx shyb qoqt")
        connection.sendmail(
            from_addr = "huytton119@gmail.com",
            to_addrs= "huytton119@gmail.com",
            msg = f"Subject: Amazon Price Alert!\n\n{message}\n{LIVE_URL}".encode("utf-8")
        )