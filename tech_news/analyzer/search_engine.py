from ..database import search_news
from datetime import datetime
import re


def search_by_title(title: str):
    news_list = list()
    query = {"title": {"$regex": title.lower()}}

    for news in search_news(query):
        news_list.append((news["title"], news["url"]))

    return news_list


def format_date(date):
    rgx = r"\d{4}-\d{2}-\d{2}"

    try:
        if re.match(rgx, date):
            return datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        else:
            raise Exception

    except (Exception):
        raise ValueError("Data com formato inválido")


def search_by_date(date):
    news_list = list()
    formated_date = format_date(date)

    query = {"timestamp": formated_date}

    for news in search_news(query):
        news_list.append((news["title"], news["url"]))

    return news_list


def search_by_category(category):
    rgx = re.compile(category, re.IGNORECASE)

    news_list = list()
    query = {"category": {"$regex": rgx}}

    for news in search_news(query):
        news_list.append((news["title"], news["url"]))

    return news_list
