# 经典算法：猜数字游戏（完整版）
# 综合运用 random、循环、异常处理

import random

secret = random.randint(1, 100)
attempts = 0
low, high = 1, 100

print("我已经想好了一个 1~100 之间的数字，来猜猜看吧！")

while True:
    try:
        guess = int(input(f"请输入你的猜测（{low}~{high}）："))
    except ValueError:
        print("请输入一个整数！")
        continue

    attempts += 1
    if guess < low or guess > high:
        print(f"请在 {low}~{high} 范围内猜测！")
        continue
    elif guess < secret:
        low = guess + 1
        print("太小了！")
    elif guess > secret:
        high = guess - 1
        print("太大了！")
    else:
        print(f"恭喜猜中！答案是 {secret}，你用了 {attempts} 次。")
        break
