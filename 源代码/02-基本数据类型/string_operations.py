# 第二章示例：字符串操作
# 演示索引、切片、操作符、常用方法

s = "HelloWorld"
print("原始字符串：", s)

print("\n=== 索引 ===")
print("s[0] =", s[0])
print("s[-1] =", s[-1])
print("s[-5] =", s[-5])

print("\n=== 切片（含头不含尾） ===")
print("s[0:5] =", s[0:5])
print("s[5:] =", s[5:])
print("s[::2] =", s[::2])
print("s[::-1] =", s[::-1])

print("\n=== 操作符 ===")
print("'ab' + 'cd' =", "ab" + "cd")
print("'ab' * 3 =", "ab" * 3)
print("'a' in 'abc' =", "a" in "abc")

print("\n=== 常用方法 ===")
s2 = "  Hello, World  "
print("len =", len(s2))
print("strip 后 =", s2.strip())
print("upper =", s2.upper())
print("lower =", s2.lower())
print("split =", s2.strip().split(","))
print("replace =", s2.replace("World", "HBUE"))
print("count('l') =", s2.count("l"))
print("startswith('He') =", s2.strip().startswith("He"))
