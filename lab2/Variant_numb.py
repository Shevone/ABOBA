a, b = [int(x) for x in input("Введите дату раождения и номер месяца: ").split()]
c =(a+b)%4
print(c+1)