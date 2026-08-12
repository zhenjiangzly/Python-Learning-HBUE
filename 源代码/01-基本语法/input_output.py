# 第一章示例：基本输入输出
# 演示 input()、eval()、print() 的用法

# 1. input() 永远返回字符串
name = input("请输入你的姓名：")
print("你好，" + name)

# 2. 数值输入需要类型转换
age = int(input("请输入年龄："))
next_year = age + 1
print("明年你", next_year, "岁")

# 3. eval() 自动识别输入类型
num = eval(input("请输入一个数字（整数或小数）："))
print("你输入的数字是：", num, "，类型是：", type(num))

# 4. print() 的 sep 和 end 参数
print("HBUE", "Python", "学习中心", sep="-")
print("第一行", end="")
print("第二行")
