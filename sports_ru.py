import requests
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver


def get_page_data(driver, url):
    driver.get(url)

    lines = driver.find_elements_by_css_selector("a[data-content-name=stats]")
    for x in lines:
        print(x.text)
    # lines = lines.find_element_by_class_name("piwikTrackContent piwikContentIgnoreInteraction")


def main():
    url = 'https://www.sports.ru/'
    driver = webdriver.Chrome('chromedriver.exe')
    lines = get_page_data(driver, url)
    driver.quit()


if __name__ == '__main__':
    main()