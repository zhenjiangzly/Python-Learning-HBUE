# 7-4 经济发展预警
last = float(input())
cur = float(input())
if cur < last * 0.7:
    print("GDP增速不足，经济过冷！")
elif cur > last * 2:
    print("GDP增速过速，经济过热！")
else:
    print("GDP增速平稳，达到预期！")
