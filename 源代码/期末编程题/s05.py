# 7-5 统计大小写英文字母的个数
s = input()
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())
print(f"句子中的大写字母有{upper}个。")
print(f"句子中的小写字母有{lower}个。")
