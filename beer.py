#!/usr/bin/python3
# coding=UTF-8

import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')

import requests
from bs4 import BeautifulSoup

url = "https://spb.bar"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

rows = soup("tr")
prices = [int(row("td")[-1].text[:-2]) for row in rows]

mean = sum(prices)/len(prices)

print("🍺 · " + str(round(mean)) + "₽")
print("🍺 ⥶ " + str(min(prices)) + "₽")
