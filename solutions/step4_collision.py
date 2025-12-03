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
# 创建游戏窗口
# ======================

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#1a1a2e")
screen.title("太空陨石躲避游戏")
screen.tracer(0)

# ======================
# 创建星空背景
# ======================

for i in range(50):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.color("white")
    star.setposition(random.randint(-390, 390), random.randint(-290, 290))
    star.dot(random.randint(1, 3))

# ======================
# 创建玩家飞船
# ======================

player = turtle.Turtle()
player.shape("triangle")
player.color("#00d4ff")
player.shapesize(1.5, 1.5)
player.penup()
player.setposition(0, -200)
player.setheading(90)

# ======================
# 飞船移动函数
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
# 创建陨石
# ======================

asteroid = turtle.Turtle()
asteroid.shape("circle")
asteroid.color("#ff6b6b")
asteroid.shapesize(1.2, 1.2)
asteroid.penup()
asteroid.setposition(random.randint(-380, 380), 300)
asteroid.dy = -3

# ======================
# 游戏结束显示
# ======================

game_over_display = turtle.Turtle()
game_over_display.color("#ff6b6b")
game_over_display.penup()
game_over_display.hideturtle()

def show_game_over():
    game_over_display.setposition(0, 20)
    game_over_display.write("💥 游戏结束 💥", align="center", font=("Arial", 36, "bold"))
    game_over_display.setposition(0, -30)
    game_over_display.color("white")
    game_over_display.write("点击屏幕退出", align="center", font=("Arial", 16, "normal"))

# ======================
# 碰撞检测函数
# ======================

def check_collision():
    if player.distance(asteroid) < 25:
        return True
    return False

# ======================
# 游戏主循环
# ======================

game_over = False

while not game_over:
    y = asteroid.ycor()
    y = y + asteroid.dy
    asteroid.sety(y)
    
    if y < -300:
        asteroid.setposition(random.randint(-380, 380), 300)
    
    if check_collision():
        game_over = True
        show_game_over()
    
    screen.update()
    time.sleep(0.01)

screen.exitonclick()

