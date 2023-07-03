# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго 
# множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите чило N: "))
m = int(input("Введите чило M: "))
union_n = set()
union_m = set()
for i in range(0,n):
    union_n.add(int(input(f"Введите {i+1} чило множества N: ")))
for i in range(0,m):
    union_m.add(int(input(f"Введите {i+1} чило множества M: ")))
my_list = list(union_n.intersection(union_m))
for i in range(1, len(my_list)):
    for j in range(1, len(my_list)):
        if my_list[j - 1] > my_list [j]:
            temp_elem = my_list[j - 1]
            my_list[j - 1] = my_list [j]
            my_list [j] = temp_elem
print(my_list)