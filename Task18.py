# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите кол-во элементов в массиве: "))
a = []
max_small = 0
min_big = 0
for i in range(0, n):
    a.append(int(input(f"Введите {i+1} элемент: ")))
    if a[i] > min_big:
        min_big = a[i]
x = int(input("Введите число Х: "))
for elem in a:
    if elem < x:
        if elem > max_small:
            max_small = elem
    elif elem > x:
        if elem < min_big:
            min_big = elem
if min_big - x <= x - max_small:
    print(min_big)
else:
    print(max_small)