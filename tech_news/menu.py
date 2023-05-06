from .analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from .analyzer.ratings import top_5_categories
from .scraper import get_tech_news
import sys


def get_tech_news_init():
    amount = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(amount)


def search_by_title_init():
    title = str(input("Digite o título: "))
    return search_by_title(title)


def search_by_date_init():
    date = str(input("Digite a data no formato aaaa-mm-dd: "))
    return search_by_date(date)


def search_by_category_init():
    category = str(input("Digite a categoria: "))
    return search_by_category(category)


def get_top_5_categories_init():
    return top_5_categories()


def exit():
    return "Encerrando script"


def get_options(current_option):
    options = {
        0: get_tech_news_init,
        1: search_by_title_init,
        2: search_by_date_init,
        3: search_by_category_init,
        4: get_top_5_categories_init,
        5: exit,
    }

    if current_option not in options:
        raise KeyError()

    else:
        print(options[current_option]())


def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n "
        "4 - Listar top 5 categorias;\n 5 - Sair."
    )

    try:
        current_option = int(input())
        get_options(current_option)

    except (ValueError, KeyError):
        sys.stderr.write("Opção inválida\n")
