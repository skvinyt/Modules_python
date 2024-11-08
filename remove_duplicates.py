def remove_duplicates(input_string):
    # Проверяем, пуста ли строка
    if not input_string:
        return input_string

    # Создаем список для хранения результата
    result = [input_string[0]]

    # Проходим по каждому символу строки, начиная со второго
    for char in input_string[1:]:
        # Сравниваем текущий символ с последним символом в списке результата
        if char != result[-1]:
            # Если они не равны, добавляем текущий символ в список
            result.append(char)

    # Преобразуем список символов в строку
    return ''.join(result)

# Пример использования функции
if __name__ == "__main__":
    input_string = "aabbccaa"
    result = remove_duplicates(input_string)
    print(result)  # Вывод: "abca"