# ======================
# Step 2: 飞船移动控制
# ======================
# 学习目标：
# - 定义函数
# - 获取和设置坐标
# - 绑定键盘事件
# - 设置边界限制

import turtle
import random

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
# 任务1：定义飞船移动函数
# ======================

# 向左移动
def move_left():
    # 获取当前x坐标
    x = player.xcor()
    
    # TODO: 边界检查 - 如果 x 大于 -380，才能向左移动
    if x > ______:
        # TODO: 向左移动20像素（x 减小）
        player.setx(x - ______)

# 向右移动
def move_right():
    x = player.xcor()
    
    # TODO: 边界检查 - 如果 x 小于 380，才能向右移动
    if x < ______:
        # TODO: 向右移动20像素（x 增加）
        player.setx(x + ______)

# 向上移动
def move_up():
    # TODO: 获取当前y坐标
    y = player.______()
    
    # 边界检查
    if y < 200:
        # TODO: 向上移动20像素（y 增加）
        player.sety(y + ______)

# 向下移动
def move_down():
    y = player.ycor()
    
    # TODO: 边界检查 - 如果 y 大于 -280
    if y > ______:
        # TODO: 向下移动20像素（y 减小）
        player.sety(y - ______)

# ======================
# 任务2：绑定键盘事件
# ======================

screen.listen()  # 开始监听键盘

# TODO: 绑定方向键到对应的函数
# 格式：screen.onkeypress(函数名, "按键名")
screen.onkeypress(move_left, "Left")
screen.onkeypress(______, "Right")      # 绑定右箭头
screen.onkeypress(______, "Up")         # 绑定上箭头
screen.onkeypress(______, "Down")       # 绑定下箭头

# 也可以用 WASD 键
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")

# ======================
# 游戏主循环
# ======================

while True:
    screen.update()


# ======================
# 🎯 完成后的挑战
# ======================
# 1. 把移动速度从 20 改成 30，感受区别
# 2. 想一想：为什么要检查 x > -380？如果不检查会怎样？
# 3. 试着让飞船移动得更快

