# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# ё первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def prg(a1, d, n):
    for i in range(n):
        print(a1+i*d)
a1=int(input("Введите a1: "))
n=int(input("Введите количество элементов: "))
d=int(input("Введите d: "))
print(prg(a1, d, n))