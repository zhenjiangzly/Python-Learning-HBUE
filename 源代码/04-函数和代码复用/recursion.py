# 第四章示例：递归
# 递归必须有结束条件

def factorial(n):
    """阶乘：n! = n * (n-1)!"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fib(n):
    """斐波那契数列第 n 项"""
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def digit_sum(n):
    """各位数字之和"""
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)


def hanoi(n, a, b, c):
    """汉诺塔：把 n 个盘子从 a 移到 c，借助 b"""
    if n == 1:
        print(f"{a} -> {c}")
    else:
        hanoi(n - 1, a, c, b)
        print(f"{a} -> {c}")
        hanoi(n - 1, b, a, c)


print("5! =", factorial(5))

print("斐波那契前10项：", end="")
for i in range(1, 11):
    print(fib(i), end=" ")
print()

print("12345 的各位和 =", digit_sum(12345))

print("3 层汉诺塔：")
hanoi(3, "A", "B", "C")
