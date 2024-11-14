from bs4 import BeautifulSoup
import requests

PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(PRACTICE_URL)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
print(price)

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)