# 第三章示例：循环嵌套与异常处理

print("=== 九九乘法表 ===")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i * j}", end="\t")
    print()

print("\n=== 用循环 else 判断素数 ===")
n = int(input("请输入一个整数："))
for i in range(2, n):
    if n % i == 0:
        print(f"{n} 不是素数")
        break
else:
    print(f"{n} 是素数")

print("\n=== try-except-else-finally ===")
try:
    a = int(input("请输入被除数："))
    b = int(input("请输入除数："))
    result = a / b
except ZeroDivisionError:
    print("除数不能为 0")
except ValueError:
    print("请输入整数")
else:
    print("计算结果：", result)
finally:
    print("finally：无论是否出错都会执行")
