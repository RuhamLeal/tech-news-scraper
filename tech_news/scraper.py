import time
import requests


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


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
