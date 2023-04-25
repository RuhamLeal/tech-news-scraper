from bs4 import BeautifulSoup as bs
from .database import create_news
import time
import requests
import re


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


def scrape_next_page_link(html_data):
    soup = bs(html_data, "html.parser")
    next_link = soup.find("a", {"class": "next page-numbers"})

    if not next_link:
        return None

    return next_link["href"]


def scrape_news(html_data):
    soup = bs(html_data, "html.parser")
    url = soup.find("div", {"class": "pk-share-buttons-wrap"})[
        "data-share-url"
    ]
    title = (soup.find("h1", {"class": "entry-title"}).text).strip()
    timestamp = soup.find("li", {"class": "meta-date"}).text
    writer = soup.find("span", {"class": "author"}).text
    reading_time = int(re.sub(
        "\D",
        "",
        soup.find("li", {"class": "meta-reading-time"}).text)
    )
    summary = (soup.find("div", {"class": "entry-content"}).p.text).strip()
    category = (
        soup.find("a", {"class": "category-style"})
        .find("span", {"class": "label"})
        .text
    )

    return dict(
        title=title,
        url=url,
        writer=writer,
        timestamp=timestamp,
        reading_time=reading_time,
        summary=summary,
        category=category,
    )


def get_range(amount, counter, news_qty):
    sum = counter + news_qty

    if sum > amount:
        range = news_qty - (sum - amount)
        return range

    return news_qty


def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news_list = list()
    counter = 0

    while counter < amount:
        html_data = fetch(url)
        news_urls = scrape_updates(html_data)
        range = get_range(amount, counter, len(news_urls))

        for url in news_urls[:(range)]:
            news_page_html_content = fetch(url)
            news_list.append(scrape_news(news_page_html_content))

        counter += range
        url = scrape_next_page_link(html_data)
        if not url:
            break

    create_news(news_list)
    return news_list
