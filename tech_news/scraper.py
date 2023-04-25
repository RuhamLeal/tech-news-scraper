import time
import requests
from bs4 import BeautifulSoup as bs


def fetch(url):
    timeout_in_seconds = 3
    headers = {"user-agent": "Fake user-agent"}
    sleep_time_in_seconds = 1

    try:
        response = requests.get(
            url,
            timeout=timeout_in_seconds,
            headers=headers,
        )
        response.raise_for_status()
        time.sleep(sleep_time_in_seconds)

    except (requests.HTTPError, requests.ReadTimeout):
        return None

    else:
        return response.text


def scrape_updates(html_data):
    soup = bs(html_data, "html.parser")
    headers = soup.find_all("h2", {"class": "entry-title"})
    urls = list()

    for header in headers:
        url = header.find("a")["href"]
        urls.append(url)

    return urls


# Requisito 3
def scrape_next_page_link(html_data):
    soup = bs(html_data, "html.parser")
    next_link = soup.find("a", {"class": "next page-numbers"})

    if not next_link:
        return None

    return next_link["href"]


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
