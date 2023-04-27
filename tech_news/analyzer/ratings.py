from .search_engine import search_by_category
from ..database import find_news


def find_all_categories():
    categories = set()

    for new in find_news():
        categories.add(new["category"])

    return categories


def top_5_categories():
    categories = find_all_categories()
    evaluations = list()

    for category in categories:
        category_qty = tuple((category, len(search_by_category(category))))
        evaluations.append(category_qty)

    evaluations.sort(key=lambda a: (-a[1], a[0]))

    return [evaluation[0] for evaluation in evaluations[:5]]
