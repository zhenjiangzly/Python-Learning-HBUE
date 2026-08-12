# 第六章示例：CSV 文件读写
# 演示一维/二维数据与 CSV 格式

# 1. 二维数据（学生成绩表）
data = [
    ["姓名", "语文", "数学"],
    ["张三", 90, 85],
    ["李四", 88, 92],
    ["王五", 70, 75],
]

print("=== 手动写入 CSV ===")
with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    for row in data:
        f.write(",".join(map(str, row)) + "\n")
print("已写入 scores.csv")

print("\n=== 手动读取 CSV ===")
with open("scores.csv", "r", encoding="utf-8") as f:
    for line in f:
        row = line.strip().split(",")
        print(row)

print("\n=== 用 csv 模块读取 ===")
import csv
with open("scores.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头
    for name, chinese, math in reader:
        total = int(chinese) + int(math)
        print(f"{name} 总分：{total}")

print("\n=== 用 csv 模块写入 ===")
with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "总分"])
    writer.writerows([["张三", 175], ["李四", 180], ["王五", 145]])
print("已写入 out.csv")

# 清理测试文件
import os
os.remove("scores.csv")
os.remove("out.csv")
