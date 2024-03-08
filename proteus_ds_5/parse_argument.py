import argparse


def parse_argument():
    """
    Функция для обработки аргумента при запуске скрипта.

    Returns
    -------
    argparse.Namespace
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('image', help='Path to the image')
        args = parser.parse_args()
        return args
    except Exception as e:
        raise Exception(f"Ошибка при обработке аргумента: {e}")
