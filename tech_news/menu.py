import sys


def get_second_step_options(first_step_option):
    second_step_options = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a categoria:",
        4: "Listando top 5 categorias...",
        5: "Saindo...",
    }

    if first_step_option not in second_step_options:
        raise KeyError()

    else:
        print(second_step_options[first_step_option])


def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n "
        "4 - Listar top 5 categorias;\n 5 - Sair."
    )

    try:
        current_option = int(input())
        get_second_step_options(current_option)

    except (ValueError, KeyError):
        sys.stderr.write("Opção inválida")
