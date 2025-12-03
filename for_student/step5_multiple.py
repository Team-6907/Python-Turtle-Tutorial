# ======================
# Step 5: 多颗陨石
# ======================
# 学习目标：
# - 使用列表存储多个对象
# - for 循环批量创建对象
# - for 循环批量操作对象
# - 函数封装

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
# 任务1：创建陨石列表和颜色列表
# ======================

# 陨石颜色列表（让陨石更多样）
asteroid_colors = ["#ff6b6b", "#ffa502", "#ff7f50", "#ee5a24", "#ff4757"]

# TODO: 创建一个空列表来存储所有陨石
asteroids = ______

# ======================
# 任务2：定义创建陨石的函数
# ======================

def create_asteroid():
    """创建一颗新陨石并添加到列表"""
    asteroid = turtle.Turtle()
    asteroid.shape("circle")
    
    # TODO: 使用 random.choice() 从颜色列表中随机选一个
    asteroid.color(random.choice(______))
    
    asteroid.shapesize(random.uniform(0.8, 1.5))  # 随机大小
    asteroid.penup()
    
    # 随机位置（在屏幕上方）
    x = random.randint(-380, 380)
    y = random.randint(300, 500)  # 错开高度
    asteroid.setposition(x, y)
    
    # 随机速度
    asteroid.dy = random.uniform(-2, -4)
    
    # TODO: 把新创建的陨石添加到列表中
    # 使用 列表.append(元素)
    asteroids.______(asteroid)

# ======================
# 任务3：批量创建5颗陨石
# ======================

# TODO: 使用 for 循环创建 5 颗陨石
# 提示：for _ in range(5): 表示执行5次
for _ in range(______):
    create_asteroid()

# ======================
# 任务4：移动所有陨石的函数
# ======================

def move_asteroids():
    """移动列表中的所有陨石"""
    # TODO: 使用 for 循环遍历 asteroids 列表
    for asteroid in ______:
        y = asteroid.ycor()
        y = y + asteroid.dy
        asteroid.sety(y)
        
        # 超出屏幕底部时重置
        if y < -300:
            x = random.randint(-380, 380)
            asteroid.setposition(x, random.randint(300, 400))
            asteroid.dy = random.uniform(-2, -4)

# ======================
# 任务5：修改碰撞检测函数
# ======================

def check_collision():
    """检测飞船是否碰到任何一颗陨石"""
    # TODO: 遍历 asteroids 列表，检查每一颗
    for asteroid in ______:
        # 如果飞船和这颗陨石距离小于25，返回True
        if player.distance(asteroid) < 25:
            return ______
    
    # 检查完所有陨石都没碰到，返回False
    return False

# ======================
# 游戏结束显示（已完成）
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
# 游戏主循环
# ======================

game_over = False

while not game_over:
    
    # --- 移动所有陨石 ---
    move_asteroids()
    
    # --- 碰撞检测 ---
    if check_collision():
        game_over = True
        show_game_over()
    
    # --- 刷新画面 ---
    screen.update()
    time.sleep(0.01)

screen.exitonclick()


# ======================
# 🤔 思考题
# ======================
# 1. 为什么要用列表 asteroids = []？
# 2. for _ in range(5) 里的 _ 是什么意思？
# 3. for asteroid in asteroids 是什么意思？

# ======================
# 🎯 完成后的挑战
# ======================
# 1. 修改 range(5) 为 range(10)，创建更多陨石
# 2. 修改 asteroid_colors 列表，添加你喜欢的颜色
# 3. 修改 random.uniform(-2, -4) 的范围，让陨石更快或更慢

