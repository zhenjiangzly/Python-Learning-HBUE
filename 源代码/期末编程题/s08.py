# 7-8 求数列和：2/1, 3/2, 5/3, 8/5, ... 斐波那契相邻项比值
n = int(input())
a, b = 1, 2
total = 0.0
for _ in range(n):
    total += b / a
    a, b = b, a + b
print(f"前{n}项之和为{total:.2f}")
