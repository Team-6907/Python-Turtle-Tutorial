# ======================
# 🚀 太空陨石躲避游戏 - 完整版
# ======================
# 这是课程的最终成果！
# 包含所有功能：星空背景、飞船控制、多颗陨石、
# 碰撞检测、计分系统、难度递增

import turtle
import random
import time

# ======================
# 游戏配置（可自定义）
# ======================

SHIP_COLOR = "#00d4ff"          # 飞船颜色
MOVE_SPEED = 20                 # 移动速度
ASTEROID_COUNT = 6              # 初始陨石数量
BASE_SPEED = 3                  # 基础游戏速度
STAR_COUNT = 60                 # 星星数量

# ======================
# 游戏状态变量
# ======================

score = 0
game_over = False
last_score_time = time.time()

# ======================
# 创建游戏窗口
# ======================

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#1a1a2e")
screen.title("🚀 太空陨石躲避游戏")
screen.tracer(0)

# ======================
# 创建星空背景
# ======================

for _ in range(STAR_COUNT):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.color(random.choice(["white", "#aaaaff", "#ffffaa"]))
    star.setposition(random.randint(-395, 395), random.randint(-295, 295))
    star.dot(random.randint(1, 3))

# ======================
# 创建玩家飞船
# ======================

player = turtle.Turtle()
player.shape("triangle")
player.color(SHIP_COLOR)
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
# 飞船移动控制
# ======================

def move_left():
    x = player.xcor()
    if x > -380:
        player.setx(x - MOVE_SPEED)

def move_right():
    x = player.xcor()
    if x < 380:
        player.setx(x + MOVE_SPEED)

def move_up():
    y = player.ycor()
    if y < 200:
        player.sety(y + MOVE_SPEED)

def move_down():
    y = player.ycor()
    if y > -280:
        player.sety(y - MOVE_SPEED)

# 键盘绑定
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
# 创建陨石系统
# ======================

asteroid_colors = ["#ff6b6b", "#ffa502", "#ff7f50", "#ee5a24", "#ff4757", "#a55eea"]
asteroids = []

def create_asteroid():
    """创建一颗新陨石"""
    asteroid = turtle.Turtle()
    asteroid.shape("circle")
    asteroid.color(random.choice(asteroid_colors))
    asteroid.shapesize(random.uniform(0.8, 1.5))
    asteroid.penup()
    asteroid.setposition(random.randint(-380, 380), random.randint(300, 600))
    asteroid.dy = random.uniform(-2, -4)
    asteroids.append(asteroid)

# 初始创建陨石
for _ in range(ASTEROID_COUNT):
    create_asteroid()

def move_asteroids():
    """移动所有陨石"""
    difficulty = 1 + (score // 10) * 0.2
    
    for asteroid in asteroids:
        y = asteroid.ycor()
        y = y + asteroid.dy * difficulty
        asteroid.sety(y)
        
        # 超出屏幕重置
        if y < -320:
            asteroid.setposition(random.randint(-380, 380), random.randint(300, 450))
            asteroid.dy = random.uniform(-2, -4)
            asteroid.color(random.choice(asteroid_colors))

# ======================
# 碰撞检测
# ======================

def check_collision():
    """检测飞船与陨石碰撞"""
    for asteroid in asteroids:
        if player.distance(asteroid) < 25:
            return True
    return False

# ======================
# UI显示系统
# ======================

# 分数显示
score_display = turtle.Turtle()
score_display.color("#ffffff")
score_display.penup()
score_display.hideturtle()
score_display.setposition(-380, 260)
score_display.write(f"分数: {score}", font=("Courier", 18, "bold"))

# 难度显示
level_display = turtle.Turtle()
level_display.color("#ffaa00")
level_display.penup()
level_display.hideturtle()
level_display.setposition(280, 260)
level_display.write("难度: 1", font=("Courier", 18, "bold"))

# 游戏结束显示
game_over_display = turtle.Turtle()
game_over_display.penup()
game_over_display.hideturtle()

def update_score():
    """更新分数（每秒+1）"""
    global score, last_score_time
    
    current_time = time.time()
    if current_time - last_score_time >= 1:
        score += 1
        last_score_time = current_time
        
        # 更新显示
        score_display.clear()
        score_display.write(f"分数: {score}", font=("Courier", 18, "bold"))
        
        level = 1 + score // 10
        level_display.clear()
        level_display.write(f"难度: {level}", font=("Courier", 18, "bold"))

def show_game_over():
    """显示游戏结束画面"""
    # 标题
    game_over_display.setposition(0, 50)
    game_over_display.color("#ff6b6b")
    game_over_display.write("💥 GAME OVER 💥", align="center", font=("Arial", 40, "bold"))
    
    # 分数
    game_over_display.setposition(0, -10)
    game_over_display.color("#ffff00")
    game_over_display.write(f"最终得分: {score}", align="center", font=("Arial", 28, "bold"))
    
    # 评价
    game_over_display.setposition(0, -60)
    game_over_display.color("#88ff88")
    if score >= 50:
        comment = "🏆 太空英雄！"
    elif score >= 30:
        comment = "⭐ 优秀飞行员！"
    elif score >= 15:
        comment = "👍 继续努力！"
    else:
        comment = "💪 再来一次！"
    game_over_display.write(comment, align="center", font=("Arial", 20, "normal"))
    
    # 提示
    game_over_display.setposition(0, -100)
    game_over_display.color("white")
    game_over_display.write("点击屏幕退出", align="center", font=("Arial", 14, "normal"))

# ======================
# 游戏主循环
# ======================

while not game_over:
    # 移动陨石
    move_asteroids()
    
    # 更新分数
    update_score()
    
    # 绘制推进器
    draw_thruster()
    
    # 碰撞检测
    if check_collision():
        game_over = True
        thruster.clear()
        show_game_over()
    
    # 刷新画面
    screen.update()
    time.sleep(0.01)

# 点击退出
screen.exitonclick()

