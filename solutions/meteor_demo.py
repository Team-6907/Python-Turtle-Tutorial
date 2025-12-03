# ======================
# 🚀 太空陨石躲避游戏 - 完整版
# ======================
# 这是课程的最终成果！
# 包含所有功能：星空背景、平滑移动、射击系统、
# 多颗陨石、碰撞检测、计分系统、难度递增

import turtle
import random
import time

# ======================
# 游戏配置（可自定义）
# ======================

SHIP_COLOR = "#00d4ff"  # 飞船颜色
ASTEROID_COUNT = 6  # 初始陨石数量
STAR_COUNT = 60  # 星星数量

# 平滑移动参数
ACCELERATION = 1.2  # 加速度
FRICTION = 0.85  # 摩擦系数
MAX_SPEED = 12  # 最大速度

# 射击参数
SHOOT_COOLDOWN = 0.3  # 射击冷却时间（秒）
BULLET_SPEED = 15  # 子弹速度

# ======================
# 游戏状态变量
# ======================

score = 0
game_over = False
last_score_time = time.time()
last_shot_time = 0

# 平滑移动状态
keys_pressed = set()
player_vx = 0
player_vy = 0

# ======================
# 创建游戏窗口
# ======================

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#1a1a2e")
screen.title("🚀 太空陨石躲避游戏 - 射击版")
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
# 平滑移动系统
# ======================


def key_press(key):
    keys_pressed.add(key)


def key_release(key):
    keys_pressed.discard(key)


def update_player_movement():
    """更新飞船位置（平滑移动）"""
    global player_vx, player_vy

    # 根据按键加速
    if "Left" in keys_pressed or "a" in keys_pressed:
        player_vx -= ACCELERATION
    if "Right" in keys_pressed or "d" in keys_pressed:
        player_vx += ACCELERATION
    if "Up" in keys_pressed or "w" in keys_pressed:
        player_vy += ACCELERATION
    if "Down" in keys_pressed or "s" in keys_pressed:
        player_vy -= ACCELERATION

    # 限制最大速度
    player_vx = max(-MAX_SPEED, min(MAX_SPEED, player_vx))
    player_vy = max(-MAX_SPEED, min(MAX_SPEED, player_vy))

    # 应用摩擦力
    player_vx *= FRICTION
    player_vy *= FRICTION

    # 速度归零
    if abs(player_vx) < 0.1:
        player_vx = 0
    if abs(player_vy) < 0.1:
        player_vy = 0

    # 更新位置
    new_x = player.xcor() + player_vx
    new_y = player.ycor() + player_vy

    # 边界检测
    if -380 <= new_x <= 380:
        player.setx(new_x)
    else:
        player_vx = 0

    if -280 <= new_y <= 200:
        player.sety(new_y)
    else:
        player_vy = 0


# ======================
# 子弹系统
# ======================

bullets = []


def create_bullet():
    """创建子弹"""
    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("#ffff00")
    bullet.shapesize(0.2, 0.5)
    bullet.penup()
    bullet.setheading(90)
    bullet.setposition(player.xcor(), player.ycor() + 20)
    bullets.append(bullet)


def shoot():
    """发射子弹"""
    global last_shot_time
    current_time = time.time()
    if current_time - last_shot_time >= SHOOT_COOLDOWN:
        create_bullet()
        last_shot_time = current_time


def move_bullets():
    """移动所有子弹"""
    for bullet in bullets[:]:
        y = bullet.ycor() + BULLET_SPEED
        bullet.sety(y)
        if y > 310:
            bullet.hideturtle()
            bullets.remove(bullet)


# ======================
# 陨石系统
# ======================

asteroid_colors = ["#ff6b6b", "#ffa502", "#ff7f50", "#ee5a24", "#ff4757", "#a55eea"]
asteroids = []


def create_asteroid():
    """创建陨石"""
    asteroid = turtle.Turtle()
    asteroid.shape("circle")
    asteroid.color(random.choice(asteroid_colors))
    asteroid.shapesize(random.uniform(0.8, 1.5))
    asteroid.penup()
    asteroid.setposition(random.randint(-380, 380), random.randint(300, 600))
    asteroid.dy = random.uniform(-2, -4)
    asteroids.append(asteroid)


def reset_asteroid(asteroid):
    """重置陨石位置"""
    asteroid.setposition(random.randint(-380, 380), random.randint(300, 450))
    asteroid.dy = random.uniform(-2, -4)
    asteroid.color(random.choice(asteroid_colors))


for _ in range(ASTEROID_COUNT):
    create_asteroid()


def move_asteroids():
    """移动所有陨石"""
    difficulty = 1 + (score // 10) * 0.2
    for asteroid in asteroids:
        y = asteroid.ycor() + asteroid.dy * difficulty
        asteroid.sety(y)
        if y < -320:
            reset_asteroid(asteroid)


# ======================
# 爆炸效果
# ======================

explosions = []


def create_explosion(x, y):
    """创建爆炸"""
    exp = turtle.Turtle()
    exp.hideturtle()
    exp.penup()
    exp.setposition(x, y)
    exp.timer = 5
    explosions.append(exp)


def update_explosions():
    """更新爆炸动画"""
    for exp in explosions[:]:
        if exp.timer > 0:
            exp.clear()
            size = (6 - exp.timer) * 6
            exp.dot(size, "#ffaa00")
            exp.timer -= 1
        else:
            exp.clear()
            explosions.remove(exp)


# ======================
# 碰撞检测
# ======================


def check_bullet_hit():
    """子弹击中陨石"""
    global score
    for bullet in bullets[:]:
        for asteroid in asteroids:
            if bullet.distance(asteroid) < 20:
                score += 5
                bullet.hideturtle()
                bullets.remove(bullet)
                create_explosion(asteroid.xcor(), asteroid.ycor())
                reset_asteroid(asteroid)
                break


def check_player_collision():
    """飞船碰撞陨石"""
    for asteroid in asteroids:
        if player.distance(asteroid) < 25:
            return True
    return False


# ======================
# UI显示系统
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
level_display.write("难度: 1", font=("Courier", 18, "bold"))

tip_display = turtle.Turtle()
tip_display.color("#88ff88")
tip_display.penup()
tip_display.hideturtle()
tip_display.setposition(0, 260)
tip_display.write("WASD移动 空格射击", font=("Courier", 12, "bold"))

game_over_display = turtle.Turtle()
game_over_display.penup()
game_over_display.hideturtle()


def update_score():
    """更新分数"""
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


def show_game_over():
    """游戏结束画面"""
    game_over_display.setposition(0, 50)
    game_over_display.color("#ff6b6b")
    game_over_display.write(
        "💥 GAME OVER 💥", align="center", font=("Arial", 40, "bold")
    )

    game_over_display.setposition(0, -10)
    game_over_display.color("#ffff00")
    game_over_display.write(
        f"最终得分: {score}", align="center", font=("Arial", 28, "bold")
    )

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

    game_over_display.setposition(0, -100)
    game_over_display.color("white")
    game_over_display.write(
        "点击屏幕退出", align="center", font=("Arial", 14, "normal")
    )


# ======================
# 键盘绑定
# ======================

screen.listen()

# 方向键 - 按下/松开
screen.onkeypress(lambda: key_press("Left"), "Left")
screen.onkeypress(lambda: key_press("Right"), "Right")
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Left"), "Left")
screen.onkeyrelease(lambda: key_release("Right"), "Right")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Down"), "Down")

# WASD - 按下/松开
screen.onkeypress(lambda: key_press("a"), "a")
screen.onkeypress(lambda: key_press("d"), "d")
screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")
screen.onkeyrelease(lambda: key_release("a"), "a")
screen.onkeyrelease(lambda: key_release("d"), "d")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeyrelease(lambda: key_release("s"), "s")

# 射击
screen.onkeypress(shoot, "space")

# ======================
# 游戏主循环
# ======================

while not game_over:
    update_player_movement()
    move_asteroids()
    move_bullets()
    check_bullet_hit()
    update_explosions()
    update_score()
    draw_thruster()

    if check_player_collision():
        game_over = True
        thruster.clear()
        tip_display.clear()
        show_game_over()

    screen.update()
    time.sleep(0.01)

screen.exitonclick()
