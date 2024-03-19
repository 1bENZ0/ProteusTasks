import argparse


def parse_argument() -> argparse.Namespace:
    """
    Функция для обработки аргумента при запуске скрипта.

    Returns
    -------
    argparse.Namespace
        Аргументы полученные из строки.
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('image', help='Path to the image')
        args = parser.parse_args()
        return args
    except Exception as e:
        raise Exception(f"Ошибка при обработке аргумента: {e}")
