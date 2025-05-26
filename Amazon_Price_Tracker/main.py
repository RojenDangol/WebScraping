import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_PASSWORD']

URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=headers)
content = response.text

soup = BeautifulSoup(content, "lxml")
# print(soup.prettify())
whole_price_tag = soup.find(name="span", class_="a-price-whole").getText().strip()
fraction_price = soup.find(name="span", class_="a-price-fraction").getText().strip()
price = float(whole_price_tag+'.'+fraction_price)

title = soup.find(name="span", id="productTitle").getText().strip()
# print(title)

if price < 130:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{title} is now {price}\n{URL}".encode('utf-8'))
