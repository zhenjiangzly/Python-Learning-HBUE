# 第一章示例：变量与赋值
# 演示命名规则、同步赋值、交换变量

# 合法的变量名
student_name = "张三"
_score = 95
x1 = 10

# 非法变量名（取消注释会报错）
# 2name = 1        # 不能以数字开头
# my-name = 1      # 不能含连字符
# if = 1           # 保留字不能用

# 同步赋值
a, b = 1, 2
print("a =", a, "b =", b)

# 链式赋值
x = y = 0
print("x =", x, "y =", y)

# 交换变量（元组解包）
a, b = b, a
print("交换后 a =", a, "b =", b)

# 动态类型：变量类型随赋值改变
v = 10          # int
print(type(v))
v = "hello"     # str
print(type(v))
