# 7-10 列表插入（保持降序）
numlist = [100, 88, 81, 80, 75, 71, 69, 65, 60, 59, 30]
x = int(input())
numlist.append(x)
numlist.sort(reverse=True)
print(" ".join(map(str, numlist)) + " ")
