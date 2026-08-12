# 第四章示例：函数定义与参数
# 演示默认参数、关键字参数、可变参数

# 基本函数
def add(a, b):
    return a + b

print("add(3, 5) =", add(3, 5))

# 默认参数
def greet(name, msg="你好"):
    print(f"{msg}，{name}！")

greet("张三")
greet("李四", "欢迎光临")

# 关键字参数（顺序可打乱）
def info(name, age, city):
    print(name, age, city)

info(city="武汉", name="张三", age=20)

# 可变参数 *args：收集为元组
def total(*args):
    print("收到的参数：", args)
    return sum(args)

print("total(1,2,3,4) =", total(1, 2, 3, 4))

# 关键字可变参数 **kwargs：收集为字典
def show(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

show(name="张三", age=20, city="武汉")

# 多返回值（元组解包）
def calc(a, b):
    return a + b, a - b

s, d = calc(10, 4)
print("和 =", s, "差 =", d)
