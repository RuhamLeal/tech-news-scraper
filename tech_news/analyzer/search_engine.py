from ..database import search_news


def search_by_title(title: str):
    news_list = list()
    query = {"title": {"$regex": title.lower()}}

    for news in search_news(query):
        news_list.append((news["title"], news["url"]))

    return news_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
