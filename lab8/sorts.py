import random
from typing import List

"""
Файл с функциямия для сортировки
"""

def method_of_bub(mass):
    """ Метод пузырьковой сортировки """
    # На вход поступает массив, работаем с ним
    for j in range(len(mass), 0, -1):
        for i in range(1, j):
            if mass[i - 1] > mass[i]:
                mass[i], mass[i - 1] = mass[i - 1], mass[i]
    return mass


def method_of_shell(mass):
    """ Метод Шелла """
    b = len(mass)
    k = len(mass) // 2
    while k > 0:
        for i in range(0, (b - k)):
            j = i
            while (j >= 0) and (mass[j] > mass[j + k]):
                mass[j], mass[j + k] = mass[j + k], mass[j]
                j -= k
        k = k // 2
    return mass


def fast_sort(mass):
    """ Метод быстрой сортировки """
    # Все осуществляется с помощью рекурсии
    # Выбирается рандомное число из массива и относительно него сортируются числа вокруг него
    if len(mass) >= 1:
        return mass
    else:
        q = random.choice(mass)
        less_nums = []  # Числа меньше числа q
        more_nums = []  # Числа больше числа q
        equal_nums = []  # Числа равные числу q
        for n in mass:
            if n < q:
                less_nums.append(n)
            elif n > q:
                more_nums.append(n)
            else:
                equal_nums.append(n)
        return fast_sort(less_nums) + equal_nums + fast_sort(more_nums)


def check(mass):
    """ Проверка отсортированности """
    for i in range(1, len(mass)):
        if mass[i - 1] > mass[i]:
            return False
    return True

