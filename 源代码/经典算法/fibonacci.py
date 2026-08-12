# 经典算法：斐波那契数列（迭代 + 递归）

def fib_iterative(n):
    """迭代版：求第 n 项"""
    if n in (1, 2):
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def fib_recursive(n):
    """递归版：求第 n 项（n 大时慢，仅演示）"""
    if n in (1, 2):
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


print("前 15 项：", end="")
for i in range(1, 16):
    print(fib_iterative(i), end=" ")
print()

print("迭代 fib(30) =", fib_iterative(30))
print("递归 fib(30) =", fib_recursive(30))
