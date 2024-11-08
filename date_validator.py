import datetime

def _is_leap_year(year):
    """
    Защищенная функция для проверки, является ли год високосным.

    :param year: Год
    :return: True, если год високосный, иначе False
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def is_valid_date(date_str):
    """
    Функция принимает строку даты в формате DD.MM.YYYY и возвращает True,
    если дата может существовать, иначе False.

    :param date_str: Строка даты в формате DD.MM.YYYY
    :return: True, если дата корректна, иначе False
    """
    try:
        # Разделяем строку даты на день, месяц и год
        day, month, year = map(int, date_str.split('.'))

        # Проверяем, что месяц находится в диапазоне от 1 до 12
        if not (1 <= month <= 12):
            return False

        # Проверяем, что год находится в диапазоне от 1 до 9999
        if not (1 <= year <= 9999):
            return False

        # Проверяем, что день находится в диапазоне от 1 до 31
        if not (1 <= day <= 31):
            return False

        # Используем datetime для проверки корректности даты
        datetime.datetime(year, month, day)

        return True
    except (ValueError, IndexError):
        return False

# Пример использования функции
if __name__ == "__main__":
    date_str = "39.02.2020"
    result = is_valid_date(date_str)
    print(result)  # Вывод: True

    date_str = "31.04.2021"
    result = is_valid_date(date_str)
    print(result)  # Вывод: False
