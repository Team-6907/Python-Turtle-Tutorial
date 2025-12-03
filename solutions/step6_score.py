# ======================
# Step 6: 计分与难度系统
# ======================
# 学习目标：
# - 全局变量
# - 时间模块使用
# - UI文字显示
# - 难度递增设计

import turtle
import random
import time

# ======================
# 游戏配置变量
# ======================

score = 0
base_speed = 3
last_score_time = time.time()

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

# 推进器火焰效果
thruster = turtle.Turtle()
thruster.hideturtle()
thruster.penup()

def draw_thruster():
    thruster.clear()
    thruster.setposition(player.xcor(), player.ycor() - 20)
    flame_color = random.choice(["#ff6600", "#ffaa00", "#ff3300"])
    flame_size = random.randint(4, 8)
    thruster.dot(flame_size, flame_color)

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

asteroid_colors = ["#ff6b6b", "#ffa502", "#ff7f50", "#ee5a24", "#ff4757"]
asteroids = []

def create_asteroid():
    asteroid = turtle.Turtle()
    asteroid.shape("circle")
    asteroid.color(random.choice(asteroid_colors))
    asteroid.shapesize(random.uniform(0.8, 1.5))
    asteroid.penup()
    asteroid.setposition(random.randint(-380, 380), random.randint(300, 500))
    asteroid.dy = random.uniform(-2, -4)
    asteroids.append(asteroid)

for _ in range(5):
    create_asteroid()

# ======================
# 移动陨石（加入难度递增）
# ======================

def move_asteroids():
    difficulty = 1 + (score // 10) * 0.2
    
    for asteroid in asteroids:
        y = asteroid.ycor()
        y = y + asteroid.dy * difficulty
        asteroid.sety(y)
        
        if y < -300:
            asteroid.setposition(random.randint(-380, 380), random.randint(300, 400))
            asteroid.dy = random.uniform(-2, -4)

# ======================
# 碰撞检测
# ======================

def check_collision():
    for asteroid in asteroids:
        if player.distance(asteroid) < 25:
            return True
    return False

# ======================
# 分数显示
# ======================

score_display = turtle.Turtle()
score_display.color("#ffffff")
score_display.penup()
score_display.hideturtle()
score_display.setposition(-380, 260)
score_display.write(f"分数: {score}", font=("Courier", 18, "bold"))

level_display = turtle.Turtle()
level_display.color("#ffaa00")
level_display.penup()
level_display.hideturtle()
level_display.setposition(280, 260)

def update_score():
    global score, last_score_time
    
    current_time = time.time()
    if current_time - last_score_time >= 1:
        score += 1
        last_score_time = current_time
        
        score_display.clear()
        score_display.write(f"分数: {score}", font=("Courier", 18, "bold"))
        
        level = 1 + score // 10
        level_display.clear()
        level_display.write(f"难度: {level}", font=("Courier", 18, "bold"))

# ======================
# 游戏结束显示
# ======================

game_over_display = turtle.Turtle()
game_over_display.penup()
game_over_display.hideturtle()

def show_game_over():
    game_over_display.setposition(0, 40)
    game_over_display.color("#ff6b6b")
    game_over_display.write("💥 游戏结束 💥", align="center", font=("Arial", 36, "bold"))
    
    game_over_display.setposition(0, -20)
    game_over_display.color("#ffff00")
    game_over_display.write(f"最终得分: {score}", align="center", font=("Arial", 24, "bold"))
    
    game_over_display.setposition(0, -70)
    game_over_display.color("white")
    game_over_display.write("点击屏幕退出", align="center", font=("Arial", 14, "normal"))

# ======================
# 游戏主循环
# ======================

game_over = False

while not game_over:
    move_asteroids()
    update_score()
    draw_thruster()
    
    if check_collision():
        game_over = True
        show_game_over()
    
    screen.update()
    time.sleep(0.01)

screen.exitonclick()

