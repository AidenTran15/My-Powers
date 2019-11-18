import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com.au/Apple-Iphone-Silver-Trusted-seller/dp/B077PQGQ4K/ref=sr_1_1?keywords=iphone+x&qid=1574036484&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
 
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[0:6])

print(converted_price)
