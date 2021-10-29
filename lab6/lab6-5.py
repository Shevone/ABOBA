# ==============================
"""Сдесь мы импортируем"""
import os
# ===============================
"""Тут происходит описание классов и переменных в них"""
# ===============================
'''Модуль первой задачи'''
class First_task:
    def PrintRectangel(a,b,file):
        # Эта функция работает если на фход передаётся 2 значения
        f = open("%s.txt" %file, 'w') # Создаём файл с названием хранящимся в переменной "file"
        f.writelines("*"*a+ '\n')# Печтаем количество звездочек согласно первой переменной и переходим на новую строку для печати
        for i in range(b-2):# Печатаем оставшие строчки не считая первой и последней
            f.writelines("*"+(" "*(a-2))+"*" + '\n')
        f.writelines("*" * a)# Печать последней строчки
        f.close()
    def PrintSquare(a,file):
        # Эта функция аналогична предыдущей
        # Отличие лишь в том что она работает с одним значением
        f = open("%s.txt" %file, 'w')
        f.writelines("*"*5 + '\n')
        for i in range(a-2):
            f.writelines("*"+(" "*(a-2))+"*"+'\n')
        f.writelines("*" * a)
        f.close()
# ================================
'''Модуль второй и третей задачи'''
def search():
    # Эта функция делает поиск файла "input.txt"
    # Если такой файл наден то в действия приводяться функции для 3 или 2 задачи(в зависимости от введённых данных)
    global word, yes # "word" - данные считанные с клавиатуры; "yes" - кортеж из ключевых слов которые может ввести пользователь при подтверждении
    a = 0
    for root, dirs, files in os.walk('.'): # В этом цикле перебираются файлы в директории по их названиям
        for filename in files:
            if filename == "input.txt":
                # Если находится нужный файл то мы прибавляет к счётчику единицу и переходим к следующим функиям
                a += 1
                if word in task2:
                    operation_with_numb_task2()
                if word in task3:
                    operation_with_numb_task3()
        if a == 0: # Если не находится файла с нужным названием то счётчик == 0
            # Пользователю предлагается созадть нужный файл
            print("Файл с входными данными не обнаружен")
            print('Хотите ли вы создать файл "input.txt"')
            a = input()
            if a in yes:
                f = open('input.txt', 'w+')
                print("Файл успешно создан!")
            else:
                print("Как пожелаете)")

def number_analiz():
    # Эта функция проверяет что файле введены именно цифры
    f = open("input.txt", 'r')
    if f.readline().isdigit() == True:
        return True
    else:
        return False
    f.close()

def operation_with_numb_task2():
    f = open("input.txt", 'r')
    # Если фунцикя на проверку записанных данных передала значанеи "True" то переходи
    # Если значени "False" то программа напишет что данные не подходят
    if number_analiz() == True:
        sum , mult , numb,  = 0, 1, f.readline()
        numb_len, numb_int = len(numb), int(numb)
        # В цикле ниже считается сумма и произведение цифр
        for i in range(numb_len):
            a = numb_int % 10
            sum += a
            mult *= a
            numb_int //=10
        print("Число: " + numb)
        print("Количесвто цифр: " + str(numb_len))
        print("Cумма цифр: " + str(sum))
        print("Произведение цифр: " + str(mult))
    else:
        print("Данные в файле не подходят для работы программы\
               \nДанные в файле:")
        print(f.readline())
    print("================================")
    f.close()

def operation_with_numb_task3():
    # эта функция анагична функции для задачи 2
    # различия только в действиях внутри фунцкии
    f = open("input.txt", 'r')
    if number_analiz() == True:
        numb = int(f.readline())
        # Дальше происходит перебор на анлализ числа
        # Простое оно или нет (прям как в ЕГЭ))
        for i in range(2,numb+1):
            a = []
            for j in range(2,i):
                if i % j ==0:
                    a.append(j)
            if len(a) == 0:
                print(i)
    else:
        print("Данные в файле не подходят для работы программы\
               \nДанные в файле:")
        print(f.readline())
    print("================================")
    f.close()
# ================================

# ================================
"""Сдесь начинается блок вызова функций"""
# кортежи слов дял вызова задач
task1 = ("1", "постороение", "задача 1")
task2 = ("2")
task3 = ('3')
stop = ("stop","break","cnjg","стоп")
yes = ('+', 'lf', "yes", "да")
print('Напишите "help" чтобы узнать возможности.')
while True:
    # бесконечный цикл для вызова функций, которые будут решать задачи
    # Цикл прекратить если переменная "word" будет соответствовать одному из слов в кортеже "stop"
    word = input()
    if word in task1:
        print("__Задача№1__\
        \n'Прямоугольники и квадраты'")
        figure = First_task
        inp_data = [x for x in input("Введите ДВЕ или ОДНУ длины сторон фигуры: ").split()]
        if len(inp_data) == 1 and inp_data[0].isdigit() == True:

            file = input("Введите имя нового файла: ")
            figure.PrintSquare(int(inp_data[0]),file)
            print("Программа выполнена!\
                              \n=======================================")
        elif len(inp_data) == 2 and inp_data[0].isdigit() == True and inp_data[1].isdigit() == True:
            file = input("Введите имя нового файла: ")
            figure.PrintRectangel(int(inp_data[0]),int(inp_data[1]), file)
            print("Программа выполнена!\
                  \n=======================================")

        else:
            print("Данные введены неверно!\nПопробуйте еще раз.")
    elif word in task2:
        print("__Задача№2__\
                \n'Все о цифрах в числе'")
        search()
    elif word in task3:
        print("__Задача№3__\
                \n'Генератор простых чисел'")
        search()
    elif word == 'help' or word =='негр':
        print('Вы можете вызвать любую задачу путем введения номера этой задачи:\
        \nВызвать задачу "Прямоугольники и квадраты" - "1"\
        \nВызвать задачу "Все о цифрах в числе" - "2"\
        \nВызвать задачу " Генератор простых чисел" - "3"\
        \nЗавершить программу - "стоп"')
    elif word in stop:
        print("До свидания ;-)")
        break