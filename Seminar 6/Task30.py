# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

my_list = []
first = int(input("Введите первый член арифметической прогрессии: "))
d = int(input("Введите разность: "))
quantity = int(input("Введите кол-во членов прогрессии: "))
for i in range(1, quantity + 1):
    my_list.append(first + (i - 1) * d)
print(my_list)