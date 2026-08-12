# 第七章示例：random 库
# 随机数各种用法

import random

print("=== 基础随机 ===")
print("random()：", random.random())           # [0,1) 浮点数
print("randint(1,6)：", random.randint(1, 6))  # 1~6 整数（含两端）
print("uniform(1,10)：", random.uniform(1, 10))
print("randrange(0,10,2)：", random.randrange(0, 10, 2))

print("\n=== 序列操作 ===")
fruits = ["苹果", "香蕉", "橘子", "西瓜"]
print("choice：", random.choice(fruits))
print("sample(2个不重复)：", random.sample(fruits, 2))
print("choices(3个可重复)：", random.choices(fruits, k=3))

deck = list(range(1, 11))
random.shuffle(deck)
print("shuffle 后：", deck)

print("\n=== 经典应用 ===")
# 随机验证码（4位数字+字母）
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
code = "".join(random.choice(chars) for _ in range(4))
print("验证码：", code)

# 抛硬币 10 次
results = [random.choice(["正面", "反面"]) for _ in range(10)]
print("抛硬币结果：", results)

# 随机点名
names = ["张三", "李四", "王五", "赵六"]
print("被点名者：", random.choice(names))
