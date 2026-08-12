# 第三章示例：循环结构
# 演示 for/while、break、continue、else

print("=== range() 的三种用法 ===")
print(list(range(5)))            # [0,1,2,3,4]
print(list(range(1, 6)))         # [1,2,3,4,5]
print(list(range(1, 10, 2)))     # [1,3,5,7,9]

print("\n=== for 累加求和 1~100 ===")
total = 0
for i in range(1, 101):
    total += i
print("1+2+...+100 =", total)

print("\n=== while 循环 ===")
n = 10
while n > 0:
    n -= 2
    print(n, end=" ")
print()

print("\n=== break 跳出循环 ===")
for i in range(10):
    if i == 4:
        break
    print(i, end=" ")
print()

print("\n=== continue 跳过 ===")
for i in range(6):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

print("\n=== 循环 else：被 break 不执行 ===")
for i in range(3):
    if i == 1:
        break
else:
    print("正常结束")
print("break 版本结束")

print("\n=== 循环 else：正常结束执行 ===")
for i in range(3):
    print(i, end=" ")
else:
    print(" -> 循环正常结束")
