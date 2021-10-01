def get_code():
    name, surname, group = input("Введите имя, фамилию, группу через пробел: ").split()
    print('Привет, %s'%name +' '+ surname+ 'из группы %s! ' %group)
    el_poch = input('Введи свою электронную почту?')
    print("Ваш код: " + (surname[:4] + name[:4]*2 + el_poch[:4]*3).lower())

get_code()