import json
from json import JSONDecodeError

import openpyxl

import requests
from bs4 import BeautifulSoup
import json
import csv
#
url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}
#
req = requests.get(url, headers=headers)
src = req.text

with open("index.html", "w", encoding="utf=8") as file:
    file.write(src)

with open("index.html", encoding="utf=8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")


all_categories_dict = {}
for item in all_products_hrefs:
    item_text = item.text
    item_href = "https://health-diet.ru" + item.get("href")
    all_categories_dict[item_text] = item_href
#

with open("all_categories_dict.json", encoding="utf=8-sig") as file:
    all_categories = json.load(file)
    #print(all_categories)
#