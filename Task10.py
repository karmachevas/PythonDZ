n = int(input("Введите кол-во монеток: "))
coin_0 = 0
coin_1 = 0
current_coin = 2
for i in range(1, n + 1):
    current_coin = int(input(f"Введите верх {i} монетки. Если решка, нажмите - 0, если орёл - 1: "))
    if current_coin > 0:
        coin_1 += 1
    else:
        coin_0 += 1
if coin_0 < coin_1:
    print(coin_0)
else: 
    print(coin_1)