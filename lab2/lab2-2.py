# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))   # Вывод типа переменной number

float_number = 9.0
print("============================================")
# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
k=1
w='aboba'
i=[]
j=(9, 4, 6)
print(type(float_number))
print(type(k))
print(type(w))
print(type(i))
print(type(j))
print("============================================")
# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.
k=str(k)
number=float(number)
float_number=int(float_number)
print("|", k,"|", number, "|", float_number, "|")

# Изначально программа печатает тип переменной “number”.
# Затем мы добавили несколько переменных и вывели их тип.
# После мы изменили тип существующих до этого переменных