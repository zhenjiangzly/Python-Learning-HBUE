# 第三章示例：分支结构
# 演示 if/elif/else 与条件表达式

# 成绩等级判断
score = int(input("请输入成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 条件表达式（三目）
age = int(input("请输入年龄："))
status = "成年人" if age >= 18 else "未成年人"
print(status)

# 多条件组合
month = int(input("请输入月份："))
if 3 <= month <= 5:
    print("春季")
elif 6 <= month <= 8:
    print("夏季")
elif 9 <= month <= 11:
    print("秋季")
else:
    print("冬季")
