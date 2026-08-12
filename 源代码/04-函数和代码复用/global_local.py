# 第四章示例：变量作用域
# 演示局部变量、全局变量、global

x = 10  # 全局变量

print("初始全局 x =", x)


def change_local():
    x = 20  # 局部变量，不影响全局
    print("函数内 x =", x)


def change_global():
    global x  # 声明修改全局变量
    x = 30
    print("函数内修改后 x =", x)


def read_only():
    print("只读全局 x =", x)  # 函数内可以直接读取全局变量


change_local()
print("调用 change_local 后全局 x =", x)

read_only()

change_global()
print("调用 change_global 后全局 x =", x)

# 可变对象作为参数：函数内修改会反映到外部
def add_item(lst):
    lst.append(100)

nums = [1, 2, 3]
add_item(nums)
print("列表被修改：", nums)  # [1, 2, 3, 100]
