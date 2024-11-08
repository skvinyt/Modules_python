def find_unique_elements(list1, list2):
    # Преобразуем оба списка в множества
    set1 = set(list1)
    set2 = set(list2)

    # Находим элементы, уникальные для каждого множества
    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1

    # Объединяем уникальные элементы
    unique_elements = unique_to_set1 | unique_to_set2

    # Преобразуем множество уникальных элементов обратно в список
    return list(unique_elements)

# Пример использования функции
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    result = find_unique_elements(list1, list2)
    print(result)  # Вывод: [1, 2, 3, 6, 7, 8]
