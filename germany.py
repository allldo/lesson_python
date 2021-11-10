import requests
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import time
delay = 7
def get_page_data(driver, url):
    some_data = []
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }
    # myElem = WebDriverWait(driver.get(url), delay)
    driver.get(url)
    driver.implicitly_wait(10)
    button = driver.find_element_by_class_name('bt-link-list')
    button.click()
    driver.implicitly_wait(35)
    elems = driver.find_elements(By.CLASS_NAME, 'bt-open-in-overlay')
    hrefs = []
    counter = 1
    for x in elems:
        hrefs.append(x.get_attribute('href'))
    for url in hrefs:

        req = requests.get(url, headers)
        with open(f"data1/{counter}.html", "w", encoding="utf-8") as file:
            file.write(req.text)

        with open(f"data1/{counter}.html", encoding="utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        try:
            name = soup.find('div', class_='col-xs-8 col-md-9 bt-biografie-name').text
        except:
            name = 'noname'
        try:
            position = soup.find('div', class_='bt-biografie-beruf').text
        except:
            position = 'posss none'
        try:
            links = [].append(soup.find('a', class_='bt-link-extern').text)
        except:
            links = []
            links.append('empty link')

        some_data.append(
            {
                'Name': name,
                'Position': position,
                'links': links,
            }
        )
        counter+=1
        driver.implicitly_wait(35)
    with open("bundes_pussies.json", "w", encoding="utf-8") as file:
        json.dump(some_data, file, indent=4, ensure_ascii=False)


def main():
    url = 'https://www.bundestag.de/en/members'
    driver = webdriver.Chrome('chromedriver.exe')
    lines = get_page_data(driver, url)
    driver.quit()


if __name__ == '__main__':
    main()