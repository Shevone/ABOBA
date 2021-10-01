from math import sqrt
x = float(input("Введте 'x': "))

while x < 0:
    x  = float(input("Введте 'x >=0': "))
y= sqrt(x+sqrt(x+sqrt(x)))
print(y)