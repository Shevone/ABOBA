""" Циклы for используются для прохождения по заданной последовательности.
На каждой итерации переменной, определенной в цикле for, будет присваиваться следующее значение в списке
"""

# Функция range (n) возвращает список [0, 1, 2, 3, ..., n-1]
print("================================")
for i in range(5):  # для каждого числа i в диапазоне 0-4
    print(i)  # эта строка выполняется 5 раз. Первый раз i равно 0, затем 1, затем 2, затем 3, затем 4

primes = [2, 3, 5, 7]  # создание нового списка

# Выведите на экран каждый элемент из primes, используя цикл for по i
print("================================")
for i in range(len(primes)):
    print(primes[i])
print("================================")
# Перебор элементов списка возможен и без использования индекса элемента
for prime in primes:
    print(prime)
print("================================")
# --------------------------------------#


""" Строки очень похожи на списки в Python. Вы можете использовать другую строку, чтобы перебрать ее. 
"""

hello_world = "Hello, World!"

for ch in hello_world:  # печать каждого символа строки
    print(ch)
print("================================")
length = 0  # переменная length

# Используйте цикл, чтобы подсчитать, сколько символов содержит hello_world. Сохраните это число в переменной length

for y in hello_world:
    length += 1  # увеличить переменную на 1 при каждом проходе цикла

print(len(hello_world) == length)
print("================================")