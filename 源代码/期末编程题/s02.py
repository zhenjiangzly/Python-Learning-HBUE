# 7-2 员工工资计算
emp_id = input()
hours = float(input())
if hours > 120:
    income = 120 * 84 + (hours - 120) * 84 * 1.15
elif hours < 60:
    income = hours * 84 - 700
else:
    income = hours * 84
print(f"员工工号为{emp_id}，应发工资为{income}元。")
