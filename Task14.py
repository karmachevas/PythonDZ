n = int(input("Введите число N: "))
k = 0
while 2 ** k <= n:
    print(2 ** k)
    k += 1