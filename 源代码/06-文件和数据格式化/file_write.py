# 第六章示例：文件写入
# 演示 write/writelines 和不同打开模式

print("=== 'w' 模式：清空后写入 ===")
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("第一次写入\n")
print("第一次写入完成")

with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("第二次写入（覆盖！）\n")
print("第二次写入完成（原内容被清空）")

print("\n=== 'a' 模式：末尾追加 ===")
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("追加的内容\n")
print("追加完成")

print("\n=== writelines 写入多行 ===")
with open("demo.txt", "w", encoding="utf-8") as f:
    f.writelines(["第1行\n", "第2行\n", "第3行\n"])

print("\n=== 验证结果 ===")
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("\n=== 写入数字需要转字符串 ===")
with open("demo.txt", "a", encoding="utf-8") as f:
    for i in range(1, 4):
        f.write(f"数字 {i}\n")

# 清理测试文件
import os
os.remove("demo.txt")
