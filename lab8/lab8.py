"""
Работу выполнил
Рябов Николай КЭ-103
"""
# ========================================================
""" Импорт функций """
from prettytable import PrettyTable
from datetime import datetime
import random
import sorts

# ========================================================
""" Описание функций """


def create(n):
    """ Создание рандомного массива """
    mass = []
    for i in range(n):
        mass.append(random.randint(0, 5555))
    mass_s = sorted(mass)
    mass_r = sorted(mass, reverse=True)
    return mass, mass_s, mass_r


def time(mass):
    """ Время сортировки массива каждым способом """
    start = datetime.now().timestamp()
    sorts.method_of_bub(mass)
    b_time = str(datetime.now().timestamp() - start)

    start = datetime.now().timestamp()
    sorts.method_of_shell(mass)
    s_time = str(datetime.now().timestamp() - start)

    start = datetime.now().timestamp()
    sorts.fast_sort(mass)
    f_time = str(datetime.now().timestamp() - start)

    return b_time, s_time, f_time,


def table_create():
    try:
        m, ms, mr = create(int(input("Введите необходимую вам длинну массива\n")))
    except:
        print("Ошибка при вводе данных")
        return False
    else:
        table = PrettyTable()
        table.add_column("Метод", ["Метод пузырька", "Метод Шелла", "Быстрая сортировка"])
        table.add_column("Случайная", time(m))
        table.add_column("Отсортированный", time(ms))
        table.add_column("Отсортированный в обратном порядке", time(mr))
    return table, m


def file_write(filename, m, table_def):
    f = open(f"{str(filename)}.txt", "w")
    f.write(f"Количество элементов: {len(m)}\n"
            f"Случайная последовательность, сгенерированная программно:\n{m}\n"
            f"{table_def.get_string()}")
    f.close()


# ========================================================
""" Основное тело  """

if __name__ == '__main__':
    result = table_create()
    table = result[0]
    mass = result[1]
    print(table)
    file_write("output", mass, table)
