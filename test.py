import pytest

from function import fibonacci, bubble_sort, calculator


# Тесты для функции определения n чисел Фибоначчи
def test_fibonacci():
    # Проверка на корректные входные данные
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]

    # Проверка на не корректные входные данные
    with pytest.raises(TypeError):
        fibonacci('abc')
    with pytest.raises(ValueError):
        fibonacci(-1)

# Тесты для функции сортировки пузырьком
def test_bubble_sort():
    # Проверка на корректные входные данные
    assert bubble_sort([]) == []
    assert bubble_sort([4, 2, 7, 1, 5]) == [1, 2, 4, 5, 7]
    assert bubble_sort([-3, 10, 0, -1, 8]) == [-3, -1, 0, 8, 10]

    # Проверка на не корректные входные данные
    with pytest.raises(TypeError):
        bubble_sort('abc')
    with pytest.raises(TypeError):
        bubble_sort([2, 5, '7'])

# Тесты для функции калькулятора
def test_calculator():
    # Проверка на корректные входные данные
    assert calculator(2, 3, '+') == 5
    assert calculator(5, 2, '-') == 3
    assert calculator(4, 6, '*') == 24
    assert calculator(8, 4, '/') == 2

    # Проверка на не корректные входные данные
    with pytest.raises(TypeError):
        calculator(10, 3, '*')
    with pytest.raises(ZeroDivisionError):
        calculator(5, 0, '/')