# 7-3 四则运算
a = float(input())
b = float(input())
c = input()
if c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "*":
    result = a * b
elif c == "/":
    if b == 0:
        print("除数不能为0")
        exit()
    result = a / b
else:
    print("输入错误")
    exit()
print(f"{a:g}{c}{b:g}={result:.2f}")
