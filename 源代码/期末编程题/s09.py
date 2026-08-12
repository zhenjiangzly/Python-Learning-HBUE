# 7-9 求最长字符串的长度
n = int(input())
strings = [input() for _ in range(n)]
print(f"最长的字符串的长度为{max(len(s) for s in strings)}。")
