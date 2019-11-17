import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com.au/Apple-Iphone-Silver-Trusted-seller/dp/B077PMXT68/ref=sr_1_3?crid=2I2PPVIR8PGLX&keywords=iphone+x&qid=1573992096&sprefix=iphine+%2Caps%2C365&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

page = requests.get(URL, headers=headers)