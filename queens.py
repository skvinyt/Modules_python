def is_safe(queens, row, col):
    for r, c in queens:
        if r == row or c == col or abs(r - row) == abs(c - col):
            return False
    return True

def check_queens(positions):
    queens = []
    for row, col in positions:
        if not is_safe(queens, row, col):
            return False
        queens.append((row, col))
    return True

# Пример использования функции
if __name__ == "__main__":
    positions = [
        (1, 4), (2, 1), (3, 5), (4, 7),
        (5, 1), (6, 4), (7, 5), (8, 8)
    ]
    result = check_queens(positions)
    print(result)  # Вывод: True или False в зависимости от расстановки
