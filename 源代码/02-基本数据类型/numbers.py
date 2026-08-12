# 第二章示例：数字类型
# 演示 int/float/complex、运算符、数值函数

print("=== 数值运算 ===")
print("7 + 2 =", 7 + 2)
print("7 - 2 =", 7 - 2)
print("7 * 2 =", 7 * 2)
print("7 / 2 =", 7 / 2)          # 除法永远返回浮点数
print("7 // 2 =", 7 // 2)        # 整除
print("7 % 2 =", 7 % 2)          # 取余
print("2 ** 3 =", 2 ** 3)        # 幂

print("\n=== 注意整除向下取整 ===")
print("-7 // 2 =", -7 // 2)      # -4
print("7 // -2 =", 7 // -2)      # -4
print("-7 % 2 =", -7 % 2)        # 1

print("\n=== 进制 ===")
print(bin(10), oct(10), hex(10))

print("\n=== 数值函数 ===")
print("abs(-5) =", abs(-5))
print("divmod(7, 2) =", divmod(7, 2))
print("pow(2, 3) =", pow(2, 3))
print("round(3.14159, 2) =", round(3.14159, 2))
print("max(1, 9, 5) =", max(1, 9, 5))

print("\n=== 复数 ===")
z = 3 + 4j
print("实部:", z.real, "虚部:", z.imag)
