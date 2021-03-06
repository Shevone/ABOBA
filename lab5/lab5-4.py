def triangle():
    # Функция для задачи номер 1
    print("__Задача №1__")
    print("Проверка существования треугольника\nВводите данные:")
# Ввод данных
    a = input('A: ')
    b = input("B: ")
    c = input("C: ")
    if a.isdigit() != True or b.isdigit() != True or c.isdigit() != True: # Проверяем что введены цифры, а также число >=0
        print("Треугольник не существует")
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        if a >= (b + c) or b >= (a + c) or c >= (b + a ): # Свойство сторон треугольника
            print("Треугольник не существует")
        elif a==0 or b == 0 or c == 0: # Cтороны не нулевые?
            print("Треугольник не существует")
        elif a == b and b == c: # Равность сторон
            print("Треугольник равносторонний")
        elif a == b or b == c or c == a: # Равность только двух сторон
            print("Треугольник равнобедренный")
        else:
            print("Треугольник общего вида") # Если дошли сюда, значит трегуольник общего вида.
    print("===============================================")

def square():
    print("__Задача №2__")
    # Функция для задачи номер 2
    print("Квадратное уравнение.\nВведите коэфициенты:")
    a = input('A: ')
    b = input("B: ")
    c = input("C: ")
# Проверка правильности ввода
    if (len(c) > 1 and c[1].isdigit() != True) or (len(c) == 1 and c.isdigit() != True):
        print("Вы ввели недопустимое значение 'C'!")
    if (len(a) > 1 and a[1].isdigit() != True) or (len(a) == 1 and a.isdigit() != True) or a == '0':
        print("Вы ввели недопустимое значение 'A'!")
    elif (len(b) > 1 and b[1].isdigit() != True) or (len(b) == 1 and b.isdigit() != True):
        print("Вы ввели недопустимое значение 'B'!")
# Если все без ошибок, то переходим к основному блоку
    else:
        a = float(a)
        b = float(b)
        c = float(c)
        print('Уравнение:\n(' + str(a) + ')*X^2+(' + str(b) + ')*X+(' + str(c) + ') =0')
# Считаем дискриминант
        D = (b ** 2) - (4 * a * c)
# По значению дискриминанта выводи данные
        if D < 0:
# Если дискриминант отрицтелен то корней нет
            print("Количество корней: 0")
        elif D > 0:
# Если дискриминант положительный то 2 корня
            print("Количество корней: 2")
            x1 = ((-b + D ** 0.5) / (2 * a))
            x2 = ((-b - D ** 0.5) / (2 * a))
# Проверяем какой корень набольший
            if x1 < x2:
                print(x1)
                print(x2)
            else:
                print(x2)
                print(x1)
# Если дискриминант 0, то один корень
        else:
            print("Количество корней: 1")
            x = (-b) / 2 * a
            print(x)
            print(x)
    print("===============================================")


def train_arrive():
    print("__Задача №3__")
    # Эта функция для задачи номер 3
    ar_h = 0
    ar_m = 0
    days = 0
    s_min = 0
    s_hour = 0
    while True:
        # Этот цикл для считывания данных о времени отправления поезда
        inp_data = [x for x in input('Введите время ОТПРАВЛЕНИЯ поезда (через двоеточие): ').split(":")]
        # Собираем часы и минуты в массив и разделяем по ":"
        if inp_data[0].isdigit() == True and inp_data[1].isdigit() == True:
            # Проверяем что все ведено правильно. Елси да, то присваем переменным тип: числовой.
            hotp = int(inp_data[0])
            motp = int(inp_data[1])
            break
            # И выходим из цикла
        else:
            print("Вы ввели недопустиые значения.")
            # Если введено не верно, то выводим это сообщение, и цикл начинается с начала
    while True:
        # Сдесь все анологично предыдущему вводу и проверке
        hp = input("Введите количество часов в пути: ")
        mp = input("Введите количество минут в пути: ")
        if hp.isdigit() == True and mp.isdigit() == True:
            hp = int(hp)
            mp = int(mp)
            break
        else:
            print("Вы ввели недопустиые значения.")
    # Суммируем часы с часами, минуты с минутами, а так же считаем кол-во дней в пути
    s_hour = hotp + hp
    s_min = motp + mp
    days = s_hour // 24
    if s_min >= 60:
        # Если сумма минут больше или равна 60 то прибавляем к часам единицу и отнимаем у суммы 60
        s_hour += 1
        s_min = s_min - 60
    if days > 0:
        # Приведение часов в нужный вид
        ar_h = s_hour - (24 * days)
    s_min = str(s_min)
    ar_h = str(ar_h)
    # Ниже мы приводи переменные в такой вид, который нужен при выводе
    if len(s_min) == 1:
        s_min = "0" + s_min
    if len(ar_h) == 1:
        ar_h = "0" + ar_h
    print(ar_h + " hourse : " + s_min + " minutes")
    print(str(days) + "days")
    print("===============================================")

# ===============================================
# Тут мы вызываел различные задачи
sp1 = ['треугольник','1']
sp2 = ["square","квадрат","2"]
sp3 = ['поезд', 'train', "3"]
stop =["стоп","СТОП","cnjg","stop"]
print('Напишите "help" чтобы узнать команды.')

while True:# Бесконечный цикл, который прерывается словами для остановки
    # В этом алгоритме происходит считывание данных с клавиатуры для вывода задания
    j = input()
    if j in sp1:
        triangle()
    elif j in sp2:
        square()
    elif j in sp3:
        train_arrive()
    elif j in stop:
        print("До свидания ;-)")
        break
    elif j == 'help' or j =='негр':
        print('Вы можете вызвать любую задачу путем введения номера этой задачи, а так же:\
        \nВызвать задачу с треугольником - "треугольник"\
        \nВызвать задачу с решение квадратного уравнения - "квадрат"\
        \nВызвать задачу на вычисление времени прибытия поезда -"поезд"\
        \nЗавершить программу - "стоп"')
    else:
        print("Я тебя не понимаю, попробуй еще раз")

