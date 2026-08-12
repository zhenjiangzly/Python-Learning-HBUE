# 第二章示例：字符串格式化
# 演示 format() 和 f-string

name = "张三"
score = 87.5

print("=== format() 方法 ===")
print("{} 的成绩是 {}".format(name, score))
print("{1} 的成绩是 {0}".format(score, name))          # 指定顺序
print("成绩：{:.2f}".format(score))                     # 两位小数
print("{:>8} 右对齐".format("ab"))                      # 右对齐宽度8
print("{:<8} 左对齐".format("ab"))
print("{:^8} 居中".format("ab"))
print("{:05d}".format(42))                             # 补0

print("\n=== f-string（推荐） ===")
print(f"{name} 的成绩是 {score}")
print(f"成绩：{score:.1f}")
print(f"百分比：{0.876:.1%}")                           # 百分比格式

print("\n=== 转义字符 ===")
print("第一行\n第二行")
print("用\t制表符\t分隔")
print("他说：\"你好\"")
