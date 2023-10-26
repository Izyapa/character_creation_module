from math import sqrt  # noqa: F403

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Проверка на положительность числа."""
    if your_number <= 0:
        return
    root: float = calculate_square_root(your_number)
    print(message)
    print('Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {root}')


calc(25.5)