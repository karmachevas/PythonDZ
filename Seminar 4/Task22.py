# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго 
# множества. Затем пользователь вводит сами элементы множеств.
from random import randint
union_n = set(randint(1, 19) for i in range(int(input("Введите чило N: "))))
union_m = set(randint(1, 19) for i in range(int(input("Введите чило M: "))))
my_list = list(union_n.intersection(union_m))
print(union_n)
print(union_m)
print(sorted(my_list))