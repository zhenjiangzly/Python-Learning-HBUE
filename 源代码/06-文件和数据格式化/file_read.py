# 第六章示例：文件读取
# 演示 read/readline/readlines 和 with 语句

# 先创建测试文件
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("第一行数据\n")
    f.write("第二行数据\n")
    f.write("第三行数据\n")

print("=== read() 读取全部 ===")
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(repr(content))

print("\n=== readline() 逐行读取 ===")
with open("demo.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
print(repr(line1))
print(repr(line2))

print("\n=== readlines() 读取所有行 ===")
with open("demo.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)

print("\n=== for 循环逐行处理（推荐） ===")
with open("demo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("处理行：", line.strip())  # strip 去掉换行

# 清理测试文件
import os
os.remove("demo.txt")
