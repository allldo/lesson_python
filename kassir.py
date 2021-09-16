import json
import requests
import re
from bs4 import BeautifulSoup

def get_data(url):

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }
    req = requests.get(url, headers)

    with open("tickets.html", "w", encoding="utf-8") as file:
        file.write(req.text)

    with open("tickets.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    events = soup.find_all("div", class_="event-info")
    event_name = 0
    event_url_list = []
    event_list = []


    for event in events:
        event_urls = "https://kassir.kz" + event.find("h3", class_="event-teaser-title").find("a").get("href")
        event_url_list.append(event_urls)

    for event_url in event_url_list:
        req = requests.get(event_url, headers)
        event_name = event_name + 1

        with open(f"data/{event_name}.html", "w", encoding="utf-8") as file:
            file.write(req.text)

        with open(f"data/{event_name}.html", encoding="utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        try:
            name = soup.find("h1", class_="event-page-title no-mobile").text
        except Exception:
            name = "Нет названия"
        try:
            details = soup.find("div", class_="full-place").find("span", class_="event-time-right").text
        except Exception:
            details = "Нет деталей"
        try:
            spot = soup.find("div", class_="full-date").find("span", class_="event-time-right").text
        except Exception:
            spot = 'unknown'
        try:
            hours = soup.find("div", class_="full-date").find("i", class_="fa fa-event-teaser fa-clock-o").next_element.next_element.text
        except:
            hours=''

        try:
            price = soup.find("div", class_="full-price").find("span", class_="event-time-right").text
        except:
            price = 'None'
        try:
            duration = soup.find(text=re.compile("Продолжительность:")).next_element.text
        except:
            duration = 'Не известно'
        event_list.append(
            {
                "Название ": name,
                "Место проведения ": details,
                "Время проведения": spot+' '+hours,
                "Цена": price,
                "Продолжительность": duration,
            }
        )

    with open("event_data.json", "w", encoding="utf-8") as file:
        json.dump(event_list, file, indent=4, ensure_ascii=False)


get_data("https://kassir.kz")