"""
МНОЖЕСТВО в Python -  это структура данных, содержащая не повторяющиеся элементы в случайном порядке.
"""

a = set()  	# Создание пустого множества

a.add(1)  	# Добавление элемента в множество

a.add(2)

a.add(1)

print(a)  	# Объясните результат

#Мы добавили элементы в множества и вывели его

b = set('hello')  # Преобразование строки в множество


print(b)  	# Объясните результат

# Строка разбилась на символы, эти символы занеси в множество


"""
Множества удобно использовать для удаления повторяющихся элементов из списка
"""



a = ['aa','ab','aa','ba']


print(set(a))

