# 第五章示例：列表操作
# 演示列表的增删改查、排序

lst = [3, 1, 4, 1, 5, 9, 2]
print("原始列表：", lst)

print("\n=== 增加 ===")
lst.append(6)             # 末尾追加
print("append(6)：", lst)
lst.insert(0, 0)          # 指定位置插入
print("insert(0,0)：", lst)
lst.extend([7, 8])        # 批量追加
print("extend([7,8])：", lst)

print("\n=== 删除 ===")
lst.remove(1)             # 按值删除（第一个）
print("remove(1)：", lst)
lst.pop()                 # 删除末尾
print("pop()：", lst)
lst.pop(0)                # 删除指定索引
print("pop(0)：", lst)
del lst[0]
print("del lst[0]：", lst)

print("\n=== 查询 ===")
print("count(4) =", lst.count(4))
print("index(5) =", lst.index(5))
print("in 判断：", 9 in lst)

print("\n=== 排序（sort 原地 / sorted 返回新列表） ===")
a = [3, 1, 2]
b = sorted(a)
print("sorted(a) =", b, "，原列表 a =", a)
a.sort()
print("a.sort() 后 a =", a)
a.sort(reverse=True)
print("降序：", a)

print("\n=== 切片 ===")
print("lst[1:4] =", lst[1:4])
print("lst[::-1] =", lst[::-1])
