"""Практическая работа №7"""
# Для работы я взял 2 задания из edu.susu ВАРИАНТ - 1
# Так же взял несколько задач из формума, как дополнительные задачи
# =================================================================
"""Описание функций"""


def P(n, x):
    """Вычисление значений полинома Лежандра"""
    if n == 0:
        f.write('1 ')
        return 1
    elif n == 1:
        f.write(str(x) + " ")
        return x
    else:
        return (- ((n - 1) * P(n - 2, x)) + (2 * n - 1) * x * P(n - 1, x)) / n


def C(m, n):
    """Вычисление биномиальных коэффициентов"""
    if (m == 0) or (n == m):
        return 1
    else:
        return C(m, n - 1) + C(m - 1, n - 1)


def operation(n):
    """Получить из 1 число N"""
    # Задача 113652
    if n <= 0:
        # Если n становиться <= 0, значит таким способом нельзя попасть => False
        return False
    elif n == 1:
        # Если n становиться == 1, значит таким способом попасть можно => True
        return True
    elif operation(n - 5):
        return operation(n - 5)
    elif operation(n - 3):
        return operation(n - 3)


def NOD(a, b):
    """Поиск нибольшего общего делителя"""
    # Задача 199
    if b == 0:
        return a
    elif a >= b:
        return NOD(b, a % b)
    else:
        return NOD(a, b % a)


def max_number(n, md=0):
    """максимальная цифра в числовой строке"""
    # Задача 113653
    if n < 10:
        return max(n, md)
    else:
        return max_number(n // 10, max(md, n % 10))


def number_count(n, count=0):
    """"Количество цифр в строке"""
    # Задача 113654
    if len(n) == 0:
        return count
    elif not (str(n)[len(n) - 1].isdigit()):
        return number_count(n[:len(n) - 1], count)
    else:
        count += 1
        return number_count(n[:len(n) - 1], count)


# =================================================================


'''Вызов функций происходит сдесь'''
print('ВАРИАНТ №1\n'
      'P - Задание 1(Вычисление значений полинома Лежандра)\n'
      'C - Задание 4(Вычисление биномиальных коэффициентов)\n'
      'NOD - Поиск нибольшего общего делителя\n'
      'OP - Получить из 1 число N\n'
      'MAX - максимальная цифра в числовой строке\n'
      'COUNT - Количество цифр в строке\n'
      'stop - остановка запросов')
while True:
    a = input().lower()
    if a == 'stop':
        break
    elif a == 'p':
        n = (input("Введите число N: "))
        x = (input("Введите число X: "))
        if not (n.isdigit() or x.isdigit()):
            # Проверка на то, что введены именно числа
            print("Неверные данные на ввод")
        else:
            n = float(n)
            x = float(x)
            f = open("output.txt", 'w')
            f.write(str(P(3, 1)))
            f.close()
            print("Программа успешно выполнена!")

    elif a == 'c':
        n = (input("Введите число N: "))
        m = (input("Введите число X: "))
        if not (n.isdigit() or x.isdigit()):
            # Проверка на то, что введены именно числа
            print("Неверные данные на ввод")
        else:
            n = int(n)
            m = int(m)
            if not (0 <= m <= n):
                print("Неверные данные на ввод")
            else:
                print(C(m, n))
    elif a == 'op':
        n = input("Введите число в диапазоне [1;200]:\n")
        if not n.isdigit():
            # Проверка на то, что введены именно числа
            print("Неверные данные на ввод")
        else:
            n = int(n)
            if not (operation(n)):
                print("NO")
            else:
                print("YES")
    elif a == "nod":
        a = (input("Введите первое число: "))
        b = (input("Введите второе число: "))
        if not (a.isdigit() or b.isdigit()):
            # Проверка на то, что введены именно числа
            print("Неверные данные на ввод")
        else:
            a = int(a)
            b = int(b)
            print(f"Наибольший общий делитель: {NOD(a, b)}")
    elif a == "max":
        n = input("Введите ЧИСЛОВУЮ строку:\n")
        if not (n.isdigit()):
            print("Неврные данные на ввод")
        else:
            print(f'Максимальная цифра в строке: {max_number(int(n))}')
    elif a == 'count':
        n = input("Введите строку:\n")
        print(
            f'Количество цифр в строке: {number_count(n)}'
        )
    else:
        print("Неизвестная команда")
    print("============================")
