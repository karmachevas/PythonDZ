s = int(input("Введите число S: "))
p = int(input("Введите число P: "))
# x + y = S
# x * y = P
# --
# x = S - y
# x * y = P
# --
# x = S - y
# (s - y) * y = P
# --
# x = S - y
# sy - y^2 = p
# --
# x = S - y
# -y^2 + sy - p = 0
# ---
# x = S - y
# y^2 - sy + p = 0
# ---

# a = 1
# b = -s
# c = p

d = s * s - (4 * 1 * p)

x1 = (s + (d ** 0.5)) / 2
x2 = (s - (d ** 0.5)) / 2
print(int(x1))
print(int(x2))