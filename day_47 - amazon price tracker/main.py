import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
TRIGER_PRICE = 300


def send_emial_notification(message):
    my_email = "dawid.python.study@gmail.com"
    password = "uyja fkuy zero vlmu"
    to = "dawid7c@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to, msg=message.encode('utf-8'))
    

AMAZON_URL = "https://www.amazon.pl/Brandit-Uniseks-Giant-Kurtka-Zielony/dp/B005GIYAHU/ref=sr_1_5?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HHNAFL9O3SP7&dib=eyJ2IjoiMSJ9.VFK-DN9960Dtn7SAx0icqJ_zBdw9D-Ufe93qUef860gM0p6L9fOZIRK5XxBc5vREJvrAX-p-IbISjQ1mXRs3nLDv3oxsbXVHEUsm8JFz3N2tub81h3XyZezh8xwJBROiilTJvtP1YvMSkHu_ON8Oi0Va0pT4EyGHzsB8u7IrvHFqA-zy8FQkVerA53torLI88-8_NK94WPRwysqTXHOY3PsfywqQ4NMoUcqTU1xiAdCW0Va1ypxEI5Zf_SOI7bIyTpJ5-1K8xowrZij-bT6cs3Mmb420U9XFNdeB_FG82GY.46COavdlBYwhEvJef57umbkg5fzL3UF5tXU9lZrPwqM&dib_tag=se&keywords=m65&qid=1709674536&sprefix=m6%2Caps%2C100&sr=8-5&th=1&psc=1"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language":"pl-PL,pl;q=0.6",
    "sec-fetch-site":"cross-site",
    "sec-ch-ua-platform":"Windows",
    "upgrade-insecure-requests":"1",
    "sec-ch-ua":'"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "x-forwarded-proto":"https",
    "x-https":"on",
    "Request Line":"GET / HTTP/1.1",
}

r = requests.get(url=AMAZON_URL, headers=header).text


soup = BeautifulSoup(r, 'lxml')

current_price_whole = soup.find(class_='a-price-whole').getText()
current_price_fraction = soup.find(class_='a-price-fraction').getText()
current_price = current_price_whole + current_price_fraction
current_price = current_price.replace(',' , '.')
print(float(current_price))

message = f"Subject:AMAZON PRICE ALERT!! \n\n Current price for Your jacket is {current_price} PLN. \n\n Check here: {AMAZON_URL}"

if float(current_price) < TRIGER_PRICE:
    send_emial_notification(message=message)