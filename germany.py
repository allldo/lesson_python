import requests
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

from selenium import webdriver
import time
delay = 7
def get_page_data(driver, url):
    # myElem = WebDriverWait(driver.get(url), delay)
    driver.get(url)
    driver.implicitly_wait(10)
    button = driver.find_element_by_class_name('bt-link-list')
    button.click()
    driver.implicitly_wait(35)
    elems = driver.find_elements(By.CLASS_NAME, 'bt-open-in-overlay')
    counter = 0
    for x in elems:
        print(x.get_attribute('href'))
        # print(counter)
        counter+=1
    

    with open("bundes_pussies.json", "w", encoding="utf-8") as file:
        json.dump(elems, file, indent=4, ensure_ascii=False)
    # lines = driver.find_element_by_tag_name("h3")
    # for x in lines:
    #     print(x.text)
    # lines = lines.find_element_by_class_name("piwikTrackContent piwikContentIgnoreInteraction")


def main():
    url = 'https://www.bundestag.de/en/members'
    driver = webdriver.Chrome('chromedriver.exe')
    lines = get_page_data(driver, url)
    driver.quit()


if __name__ == '__main__':
    main()