# ======================
# Step 4: 碰撞检测
# ======================
# 学习目标：
# - 距离计算
# - 条件判断实现碰撞检测
# - 游戏状态管理（game_over）
# - 游戏结束画面

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
# 创建陨石（已完成）
# ======================

asteroid = turtle.Turtle()
asteroid.shape("circle")
asteroid.color("#ff6b6b")
asteroid.shapesize(1.2, 1.2)
asteroid.penup()
asteroid.setposition(random.randint(-380, 380), 300)
asteroid.dy = -3

# ======================
# 游戏结束显示（已完成）
# ======================

game_over_display = turtle.Turtle()
game_over_display.color("#ff6b6b")
game_over_display.penup()
game_over_display.hideturtle()

def show_game_over():
    """显示游戏结束画面"""
    game_over_display.setposition(0, 20)
    game_over_display.write("💥 游戏结束 💥", align="center", font=("Arial", 36, "bold"))
    game_over_display.setposition(0, -30)
    game_over_display.color("white")
    game_over_display.write("点击屏幕退出", align="center", font=("Arial", 16, "normal"))

# ======================
# 任务1：碰撞检测函数
# ======================

def check_collision():
    """
    检测飞船和陨石是否碰撞
    
    原理：计算两个对象中心点的距离
    如果距离 < 25像素，认为发生碰撞
    """
    # TODO: 使用 player.distance(asteroid) 计算距离
    # distance() 方法返回两个对象之间的像素距离
    distance = player.______(asteroid)
    
    # TODO: 如果距离小于 25，返回 True（碰撞了）
    if distance < ______:
        return True
    
    # 没碰撞，返回 False
    return False

# ======================
# 任务2：游戏主循环（添加碰撞检测）
# ======================

# TODO: 定义游戏状态变量，初始值为 False
game_over = ______

# TODO: 使用 while not game_over 作为循环条件
# 意思是"只要游戏没结束就继续"
while not ______:
    
    # --- 移动陨石 ---
    y = asteroid.ycor()
    y = y + asteroid.dy
    asteroid.sety(y)
    
    # --- 陨石重置 ---
    if y < -300:
        asteroid.setposition(random.randint(-380, 380), 300)
    
    # --- 【新增】碰撞检测 ---
    # TODO: 调用 check_collision() 函数，如果返回 True
    if ______():
        # TODO: 设置 game_over 为 True
        game_over = ______
        # 显示游戏结束画面
        show_game_over()
    
    # --- 刷新画面 ---
    screen.update()
    time.sleep(0.01)

# 游戏结束后，点击屏幕退出
screen.exitonclick()


# ======================
# 🤔 思考题
# ======================
# 1. player.distance(asteroid) 是什么意思？
# 2. 为什么用 while not game_over 而不是 while True？
# 3. 如果把碰撞距离从 25 改成 10 会怎样？

# ======================
# 🎯 完成后的挑战
# ======================
# 1. 把碰撞距离 25 改成 50，体验"更容易被撞到"
# 2. 把碰撞距离改成 10，体验"更难被撞到"
# 3. 修改 show_game_over() 里的文字内容

