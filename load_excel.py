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
iteration_count = int(len(all_categories)) - 1
count = 0

qwe = openpyxl.Workbook()
sheet = qwe.active
for category_name, category_href in all_categories.items():

    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")

    # print(category_name)


    try:
        with open(f"data/{count}_{category_name}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f'{count}')
        count += 1
        row = 2
        sheet['A1'] = 'TITLE'
        sheet['B1'] = 'CALORIES'
        sheet['C1'] = 'PROTEINS'
        sheet['D1'] = 'FATS'
        sheet['F1'] = 'CARBOHYDRATES'

        for aboba in data:
            sheet[row][0].value = aboba['Title']
            sheet[row][1].value = aboba['Calories']
            sheet[row][2].value = aboba['Proteins']
            sheet[row][3].value = aboba['Fats']
            sheet[row][4].value = aboba['Carbohydrates']
            row+=1
    except JSONDecodeError:
        print('zxc')
qwe.save('data.xlsx')

qwe.close()