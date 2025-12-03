# ======================
# Step 1: 游戏窗口与飞船
# ======================
# 学习目标：
# - 导入 turtle 库
# - 创建游戏窗口
# - 创建飞船角色
# - 添加星空背景

import turtle
import random

# ======================
# 创建游戏窗口
# ======================

screen = turtle.Screen()
screen.setup(800, 600)  # 窗口大小：宽800，高600
screen.bgcolor("#1a1a2e")  # 深蓝色背景，像太空
screen.title("太空陨石躲避游戏")
screen.tracer(0)  # 关闭自动刷新（提高性能）

# ======================
# 创建星空背景
# ======================
# 用小白点模拟星星

stars = []
for i in range(50):
    star = turtle.Turtle()
    star.hideturtle()  # 隐藏乌龟图标
    star.penup()
    star.color("white")
    # 随机位置
    x = random.randint(-390, 390)
    y = random.randint(-290, 290)
    star.setposition(x, y)
    star.dot(random.randint(1, 3))  # 画一个小点，大小1-3
    stars.append(star)

# ======================
# 创建玩家飞船
# ======================

player = turtle.Turtle()
player.shape("triangle")  # 三角形 = 飞船形状
player.color("#00d4ff")  # 青色
player.shapesize(1.5, 1.5)  # 放大1.5倍
player.penup()  # 抬起画笔（移动不画线）
player.setposition(0, -200)  # 初始位置：屏幕下方中央
player.setheading(90)  # 朝向上方

# ======================
# 刷新画面
# ======================

screen.update()

# 点击屏幕退出
screen.exitonclick()

