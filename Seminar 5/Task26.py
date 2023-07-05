# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def grade(num_a, num_b):
    if num_b == 0:
        return 1
    elif num_b == 1:
        return num_a
    else:
        return num_a * grade(num_a, num_b - 1)

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

print(f"{a} в степени {b} равно: {grade(a, b)}")