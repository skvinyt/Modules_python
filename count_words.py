import word_count

def main():
    words_list = ["apple", "banana", "apple", "orange", "banana", "banana", "banana"]
    result = word_count.count_words(words_list)
    print(result)  # Вывод: {'apple': 2, 'banana': 3, 'orange': 1}

if __name__ == "__main__":
    main()
