def count_words(words):
    word_count = {}

    for word in words:
        # Получаем текущее значение слова в словаре, если его нет, то 0
        count = word_count.get(word, 0)
        # Увеличиваем счетчик на 1
        word_count[word] = count + 1

    return word_count
