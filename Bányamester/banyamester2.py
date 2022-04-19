from bs4 import BeautifulSoup as bs
import requests
import time
import sys

url = 'https://www.google.com/search?q=etherium+%C3%A1r'
raw = requests.get(url)

parsed = bs(raw.text, 'html.parser')
sys.stdout.write(parsed.prettify())
