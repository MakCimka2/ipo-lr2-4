import math
x = float(input("Введите х "))
y = float(input("Введите у "))
z = float(input("Введите z "))
h = ((x ** (y + 1)) + (math.e ** (y - 1)) / (1 + x * abs(y - (math.tan(z))))) * (1 + abs(y - x)) + (((abs(y - x)) ** 2) / 2) -  (((abs(y - x)) ** 3) / 3)
print("Результат: h = ", h)