# 第五章示例：字典操作
# 演示字典的增删改查、遍历

d = {"name": "张三", "age": 20}
print("原始字典：", d)

print("\n=== 增加与修改 ===")
d["city"] = "武汉"        # 新增
d["age"] = 21             # 修改
print("新增 city、修改 age：", d)

print("\n=== 访问 ===")
print("d['name'] =", d["name"])
print("d.get('city') =", d.get("city"))
print("d.get('score', 0) =", d.get("score", 0))   # 键不存在返回默认值

print("\n=== 删除 ===")
d.pop("city")
print("pop('city')：", d)
del d["age"]
print("del d['age']：", d)

print("\n=== 遍历 ===")
d = {"语文": 90, "数学": 85, "英语": 92}
for k in d:
    print("键：", k)
for v in d.values():
    print("值：", v)
for k, v in d.items():
    print(k, "->", v)

print("\n=== 常用方法 ===")
print("keys：", list(d.keys()))
print("values：", list(d.values()))
print("items：", list(d.items()))
print("len：", len(d))

print("\n=== 经典应用：统计字符出现次数 ===")
text = "hello world"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
