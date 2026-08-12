# 第五章示例：元组与集合
# 演示元组的不可变性、解包、集合去重

print("=== 元组 ===")
t = (1, 2, 3)
print("t =", t)
print("t[0] =", t[0])
print("t[1:3] =", t[1:3])
print("t + (4,) =", t + (4,))
print("t * 2 =", t * 2)

# 元组不可变
try:
    t[0] = 99
except TypeError as e:
    print("修改元组报错：", e)

# 单个元素的元组必须有逗号
print("(1) 的类型：", type(1))
print("(1,) 的类型：", type((1,)))

print("\n=== 元组解包 ===")
a, b, c = (10, 20, 30)
print("a, b, c =", a, b, c)

# 交换变量是解包的经典应用
m, n = 5, 8
m, n = n, m
print("交换后 m, n =", m, n)

print("\n=== 集合 ===")
s = {1, 2, 2, 3, 3, 3}
print("集合自动去重：", s)

lst = [3, 1, 2, 3, 1, 4]
print("列表去重：", list(set(lst)))

print("交集：", {1, 2, 3} & {2, 3, 4})
print("并集：", {1, 2, 3} | {2, 3, 4})
print("差集：", {1, 2, 3} - {2, 3, 4})

s.add(5)
print("add(5) 后：", s)
