# 第七章示例：turtle 库
# 画一个彩色螺旋线

import turtle

# 设置画布和速度
turtle.setup(600, 600)
turtle.speed(10)

# 颜色列表
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# 画螺旋线
for i in range(36):
    turtle.pencolor(colors[i % 6])   # 循环取颜色
    turtle.forward(i * 5)            # 长度递增
    turtle.right(144)                # 固定转角

turtle.done()   # 保持窗口不关闭
