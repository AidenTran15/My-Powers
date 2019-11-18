import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com.au/Apple-Iphone-Silver-Trusted-seller/dp/B077PQGQ4K/ref=sr_1_1?keywords=iphone+x&qid=1574036484&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    if(converted_price < 1.000):
        send_email()

    print(converted_price)
    print(title.strip())

    if(converted_price < 1.000):
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('trantuankiett.02@gmail.com', '****************')
    subject = 'Hey, the price fell down!'
    body = 'Check the amazon link https://www.amazon.com.au/Apple-Iphone-Silver-Trusted-seller/dp/B077PQGQ4K/ref=sr_1_1?keywords=iphone+x&qid=1574036484&sr=8-1'

    msg = f"subject: {subject}\n\n{body}"
    
    server.sendmail(
        'trantuankiett.02@gmail',
        'aidenkiettran@gmail.com',
        msg
    )
    print("Hey, email has been send")

#     server.quit

check_price()






