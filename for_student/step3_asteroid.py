# ======================
# Step 3: 陨石创建与下落
# ======================
# 学习目标：
# - 使用 random 模块
# - 理解游戏主循环
# - 实现动画效果
# - 给对象添加自定义属性

import turtle
import random
import time

# ======================
# 创建游戏窗口（已完成）
# ======================

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#1a1a2e")
screen.title("太空陨石躲避游戏")
screen.tracer(0)

# ======================
# 创建星空背景（已完成）
# ======================

for i in range(50):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.color("white")
    star.setposition(random.randint(-390, 390), random.randint(-290, 290))
    star.dot(random.randint(1, 3))

# ======================
# 创建玩家飞船（已完成）
# ======================

player = turtle.Turtle()
player.shape("triangle")
player.color("#00d4ff")
player.shapesize(1.5, 1.5)
player.penup()
player.setposition(0, -200)
player.setheading(90)

# ======================
# 飞船移动函数（已完成）
# ======================

def move_left():
    x = player.xcor()
    if x > -380:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 380:
        player.setx(x + 20)

def move_up():
    y = player.ycor()
    if y < 200:
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -280:
        player.sety(y - 20)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")

# ======================
# 任务1：创建一颗陨石
# ======================

asteroid = turtle.Turtle()

# TODO: 设置陨石形状为圆形 "circle"
asteroid.shape(______)

# TODO: 设置陨石颜色为红色 "#ff6b6b"
asteroid.color(______)

asteroid.shapesize(1.2, 1.2)
asteroid.penup()

# TODO: 使用 random.randint(-380, 380) 生成随机x坐标
start_x = random.randint(______, ______)
asteroid.setposition(start_x, 300)  # y=300 是屏幕上方

# 【重要】给陨石添加一个自定义属性：下落速度
# TODO: 设置 dy 为 -3（负数表示向下）
asteroid.dy = ______

# ======================
# 任务2：游戏主循环
# ======================

while True:
    # --- 移动陨石 ---
    
    # TODO: 获取陨石当前y坐标
    y = asteroid.______()
    
    # TODO: 计算新位置（y + dy，因为dy是负数，所以会下降）
    y = y + asteroid.______
    
    # TODO: 设置陨石新的y坐标
    asteroid.______(y)
    
    # --- 陨石超出屏幕底部时，重置到顶部 ---
    if y < -300:
        # TODO: 重新随机一个x位置
        new_x = random.randint(______, ______)
        asteroid.setposition(new_x, 300)
    
    # --- 刷新画面 ---
    screen.update()
    
    # --- 控制速度 ---
    time.sleep(0.01)


# ======================
# 🤔 思考题
# ======================
# 1. 为什么陨石会"动"？
# 2. asteroid.dy = -3 是什么意思？
# 3. 如果把 time.sleep(0.01) 改成 time.sleep(0.1) 会怎样？

# ======================
# 🎯 完成后的挑战
# ======================
# 1. 修改 asteroid.dy，改成 -5 或 -1，观察速度变化
# 2. 修改陨石的颜色
# 3. 修改陨石的大小

