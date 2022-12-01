"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов."""

def my_func(a, b, c):
    numbers = [a, b, c]
    result = []
    max_1 = max(numbers)
    result.append(max_1)
    numbers.remove(max_1)
    max_2 = max(numbers)
    result.append(max_2)
    print(sum(result))
my_func(6, 2, 0)