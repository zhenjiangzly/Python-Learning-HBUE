# 7-11 列表与字符串：转大写并排序
strings = [input() for _ in range(5)]
new_list = [s.upper() for s in strings]
print(f"新列表为{new_list}")
new_list.sort()
print(f"排序后的列表为{new_list}")
