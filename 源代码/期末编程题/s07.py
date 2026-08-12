# 7-7 求特殊三位数：除以9的商 = 各位数字平方和
n = int(input())
count = 0
line = ""
for x in range(100, n + 1):
    a = x // 100
    b = x // 10 % 10
    c = x % 10
    if x // 9 == a * a + b * b + c * c:
        line += f"{x} "
        count += 1
        if count % 5 == 0:
            print(line)
            line = ""
if line:
    print(line)
