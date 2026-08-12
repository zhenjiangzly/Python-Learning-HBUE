# 7-1 输出成绩等级
score = int(input())
if score >= 90:
    rank = "等级优秀"
elif score >= 80:
    rank = "等级良好"
elif score >= 70:
    rank = "等级中等"
elif score >= 60:
    rank = "等级及格"
else:
    rank = "等级不及格"
print(f"高数成绩{score}分，{rank}")
