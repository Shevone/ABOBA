big_data = {}
def number_inp():
    n = input("Введите количество призывников: ")
    while n.isdigit() != True:
        n = input("Введите количество призывников ЧИСЛОМ: ")
    n = int(n)
    return n

def data_inp():
    dict_s = {}
    inp_data = [x for x in input('Введите: Фамилию, Имя, Отчество, Год рождения, Заболеване (через пробел): ').split()]
    while len(inp_data) != 5:
        print("Вы ввели слишком много данных, попробуйте еще разю")
        inp_data = [x for x in
                    input('Введите: Фамилию, Имя, Отчество, Год рождения, Заболеване (через пробел): ').split()]
    dict_s["Фамилия"] = inp_data[0]
    dict_s["Имя"] = inp_data[1]
    dict_s["Отчество"] = inp_data[2]
    dict_s["Год рождения"] = inp_data[3]
    dict_s["Заболевание"] = inp_data[4]
    return dict_s

def big_data_upload():
    global big_data
    a = 0
    for i in range(number_inp()):
        a += 1
        big_data['Призывник №' + str(a)] = data_inp()
    return big_data

def output():
    for i in big_data_upload():
        print(i, ' => ')
        print("Фамилия: ", big_data[i]["Фамилия"])
        print("Имя: ", big_data[i]["Имя"])
        print("Отчество: ", big_data[i]["Отчество"])
        print("Год рождения: ", big_data[i]["Год рождения"])
        print("Заболевание: ", big_data[i]["Заболевание"])
        print("====================================")

vopros = input("Если вы хотите запустить программу отправьте: '+' или напишите 'Да': ")
soglas = ["+", "Да",'да','yes','Yes','ok']
if vopros in soglas:
    output()
elif vopros == "ABOBA":
    print("ABOBA")
else:
    print("До свидания)")
