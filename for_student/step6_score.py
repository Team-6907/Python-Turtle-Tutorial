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
# 任务1：游戏配置变量
# ======================

# TODO: 定义分数变量，初始值为 0
score = ______

# 基础速度
base_speed = 3

# TODO: 记录上次得分的时间
last_score_time = time.time()

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

# 推进器火焰效果
thruster = turtle.Turtle()
thruster.hideturtle()
thruster.penup()

def draw_thruster():
    """绘制飞船推进器火焰"""
    thruster.clear()
    thruster.setposition(player.xcor(), player.ycor() - 20)
    flame_color = random.choice(["#ff6600", "#ffaa00", "#ff3300"])
    flame_size = random.randint(4, 8)
    thruster.dot(flame_size, flame_color)

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
# 任务2：移动陨石（加入难度递增）
# ======================

def move_asteroids():
    """移动陨石，速度随分数增加"""
    # TODO: 计算难度系数
    # 公式：1 + (score // 10) * 0.2
    # score // 10 是整除，得到十位数字
    # 分数0-9: 难度=1.0，分数10-19: 难度=1.2，以此类推
    difficulty = 1 + (______ // 10) * 0.2
    
    for asteroid in asteroids:
        y = asteroid.ycor()
        # TODO: 速度乘以难度系数
        y = y + asteroid.dy * ______
        asteroid.sety(y)
        
        if y < -300:
            asteroid.setposition(random.randint(-380, 380), random.randint(300, 400))
            asteroid.dy = random.uniform(-2, -4)

# ======================
# 碰撞检测（已完成）
# ======================

def check_collision():
    for asteroid in asteroids:
        if player.distance(asteroid) < 25:
            return True
    return False

# ======================
# 任务3：分数显示
# ======================

score_display = turtle.Turtle()
score_display.color("#ffffff")
score_display.penup()
score_display.hideturtle()
score_display.setposition(-380, 260)

# TODO: 显示初始分数
# 使用 f-string 格式化字符串
score_display.write(f"分数: {______}", font=("Courier", 18, "bold"))

# 难度显示
level_display = turtle.Turtle()
level_display.color("#ffaa00")
level_display.penup()
level_display.hideturtle()
level_display.setposition(280, 260)
level_display.write("难度: 1", font=("Courier", 18, "bold"))

# ======================
# 任务4：更新分数函数
# ======================

def update_score():
    """每秒增加分数"""
    # TODO: 使用 global 声明要修改的全局变量
    global ______, last_score_time
    
    current_time = time.time()
    
    # TODO: 如果当前时间 - 上次得分时间 >= 1秒
    if current_time - last_score_time >= ______:
        # TODO: 分数加1
        score += ______
        
        # 重置计时
        last_score_time = current_time
        
        # 更新分数显示
        score_display.clear()
        score_display.write(f"分数: {score}", font=("Courier", 18, "bold"))
        
        # 更新难度显示
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
    # 标题
    game_over_display.setposition(0, 40)
    game_over_display.color("#ff6b6b")
    game_over_display.write("💥 游戏结束 💥", align="center", font=("Arial", 36, "bold"))
    
    # TODO: 显示最终分数
    game_over_display.setposition(0, -20)
    game_over_display.color("#ffff00")
    game_over_display.write(f"最终得分: {______}", align="center", font=("Arial", 24, "bold"))
    
    # 提示
    game_over_display.setposition(0, -70)
    game_over_display.color("white")
    game_over_display.write("点击屏幕退出", align="center", font=("Arial", 14, "normal"))

# ======================
# 游戏主循环
# ======================

game_over = False

while not game_over:
    
    # 移动陨石
    move_asteroids()
    
    # TODO: 调用更新分数函数
    ______()
    
    # 绘制推进器火焰
    draw_thruster()
    
    # 碰撞检测
    if check_collision():
        game_over = True
        show_game_over()
    
    screen.update()
    time.sleep(0.01)

screen.exitonclick()


# ======================
# 🤔 思考题
# ======================
# 1. 为什么需要 global score？
# 2. difficulty = 1 + (score // 10) * 0.2 是什么意思？
# 3. 为什么用 time.time() 来计时？

# ======================
# 🎯 完成后的挑战
# ======================
# 1. 修改难度增长速度：把 * 0.2 改成 * 0.5
# 2. 修改得分速度：把 >= 1 改成 >= 0.5（半秒得1分）
# 3. 添加分数评价：50分以上显示"太空英雄"

