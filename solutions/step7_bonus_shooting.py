# ======================
# 🎁 Bonus: 射击功能
# ======================
# 学习目标：
# - 创建子弹系统
# - 实现子弹与陨石的碰撞检测
# - 按空格键发射子弹
# - 综合运用之前学到的所有知识

import turtle
import random
import time

# ======================
# 游戏配置
# ======================

score = 0
game_over = False
last_score_time = time.time()
last_shot_time = 0  # 上次射击时间
shoot_cooldown = 0.3  # 射击冷却时间（秒）

# ======================
# 【新增】平滑移动系统
# ======================
keys_pressed = set()  # 当前按下的键
player_vx = 0  # 水平速度
player_vy = 0  # 垂直速度
acceleration = 1.2  # 加速度
friction = 0.85  # 摩擦系数
max_speed = 12  # 最大速度

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

for _ in range(50):
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

# 推进器火焰
thruster = turtle.Turtle()
thruster.hideturtle()
thruster.penup()


def draw_thruster():
    thruster.clear()
    thruster.setposition(player.xcor(), player.ycor() - 20)
    flame_color = random.choice(["#ff6600", "#ffaa00", "#ff3300"])
    thruster.dot(random.randint(4, 8), flame_color)


# ======================
# 【改进】平滑移动系统
# ======================


def key_press(key):
    """按键按下时调用"""
    keys_pressed.add(key)


def key_release(key):
    """按键松开时调用"""
    keys_pressed.discard(key)


def update_player_movement():
    """根据按键状态更新飞船速度和位置"""
    global player_vx, player_vy

    # 根据按键加速
    if "Left" in keys_pressed or "a" in keys_pressed:
        player_vx -= acceleration
    if "Right" in keys_pressed or "d" in keys_pressed:
        player_vx += acceleration
    if "Up" in keys_pressed or "w" in keys_pressed:
        player_vy += acceleration
    if "Down" in keys_pressed or "s" in keys_pressed:
        player_vy -= acceleration

    # 限制最大速度
    player_vx = max(-max_speed, min(max_speed, player_vx))
    player_vy = max(-max_speed, min(max_speed, player_vy))

    # 应用摩擦力
    player_vx *= friction
    player_vy *= friction

    # 速度很小时归零（防止无限滑动）
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
        player_vx = 0  # 撞墙速度归零

    if -280 <= new_y <= 200:
        player.sety(new_y)
    else:
        player_vy = 0  # 撞墙速度归零


# ======================
# 【新增】子弹系统
# ======================

bullets = []  # 存储所有子弹


def create_bullet():
    """创建一颗新子弹"""
    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("#ffff00")  # 黄色子弹
    bullet.shapesize(0.2, 0.5)  # 细长的形状
    bullet.penup()
    bullet.setheading(90)  # 朝向上方
    # 从飞船位置发射
    bullet.setposition(player.xcor(), player.ycor() + 20)
    bullets.append(bullet)


def shoot():
    """发射子弹（带冷却时间）"""
    global last_shot_time

    current_time = time.time()
    # 检查冷却时间
    if current_time - last_shot_time >= shoot_cooldown:
        create_bullet()
        last_shot_time = current_time


def move_bullets():
    """移动所有子弹"""
    for bullet in bullets[:]:  # 使用切片复制列表，避免遍历时修改
        y = bullet.ycor()
        y += 15  # 子弹速度
        bullet.sety(y)

        # 超出屏幕顶部，移除子弹
        if y > 310:
            bullet.hideturtle()
            bullets.remove(bullet)


# ======================
# 陨石系统
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


def reset_asteroid(asteroid):
    """重置陨石位置"""
    asteroid.setposition(random.randint(-380, 380), random.randint(300, 450))
    asteroid.dy = random.uniform(-2, -4)
    asteroid.color(random.choice(asteroid_colors))


for _ in range(6):
    create_asteroid()


def move_asteroids():
    difficulty = 1 + (score // 10) * 0.2

    for asteroid in asteroids:
        y = asteroid.ycor()
        y += asteroid.dy * difficulty
        asteroid.sety(y)

        if y < -320:
            reset_asteroid(asteroid)


# ======================
# 【新增】子弹与陨石碰撞检测
# ======================


def check_bullet_hit():
    """检测子弹是否击中陨石"""
    global score

    for bullet in bullets[:]:
        for asteroid in asteroids:
            if bullet.distance(asteroid) < 20:
                # 击中了！
                score += 5  # 击中陨石得5分

                # 移除子弹
                bullet.hideturtle()
                bullets.remove(bullet)

                # 重置陨石
                reset_asteroid(asteroid)

                # 创建爆炸效果（简单版本）
                create_explosion(asteroid.xcor(), asteroid.ycor())

                break  # 一颗子弹只能击中一个陨石


# ======================
# 【新增】爆炸效果
# ======================

explosions = []


def create_explosion(x, y):
    """在指定位置创建爆炸效果"""
    exp = turtle.Turtle()
    exp.hideturtle()
    exp.penup()
    exp.setposition(x, y)
    exp.timer = 5  # 爆炸持续帧数
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
# 飞船与陨石碰撞检测
# ======================


def check_player_collision():
    for asteroid in asteroids:
        if player.distance(asteroid) < 25:
            return True
    return False


# ======================
# UI显示
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

# 射击提示
tip_display = turtle.Turtle()
tip_display.color("#88ff88")
tip_display.penup()
tip_display.hideturtle()
tip_display.setposition(0, 260)
tip_display.write("按空格键射击!", font=("Courier", 14, "bold"))


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
# 游戏结束
# ======================

game_over_display = turtle.Turtle()
game_over_display.penup()
game_over_display.hideturtle()


def show_game_over():
    game_over_display.setposition(0, 40)
    game_over_display.color("#ff6b6b")
    game_over_display.write(
        "💥 游戏结束 💥", align="center", font=("Arial", 36, "bold")
    )

    game_over_display.setposition(0, -20)
    game_over_display.color("#ffff00")
    game_over_display.write(
        f"最终得分: {score}", align="center", font=("Arial", 24, "bold")
    )

    game_over_display.setposition(0, -70)
    game_over_display.color("white")
    game_over_display.write(
        "点击屏幕退出", align="center", font=("Arial", 14, "normal")
    )


# ======================
# 键盘绑定（状态追踪）
# ======================

screen.listen()

# 方向键 - 按下
screen.onkeypress(lambda: key_press("Left"), "Left")
screen.onkeypress(lambda: key_press("Right"), "Right")
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")

# WASD键 - 按下
screen.onkeypress(lambda: key_press("a"), "a")
screen.onkeypress(lambda: key_press("d"), "d")
screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")

# 方向键 - 松开
screen.onkeyrelease(lambda: key_release("Left"), "Left")
screen.onkeyrelease(lambda: key_release("Right"), "Right")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Down"), "Down")

# WASD键 - 松开
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
    update_player_movement()  # 【新增】平滑移动更新
    move_asteroids()
    move_bullets()  # 移动子弹
    check_bullet_hit()  # 检测子弹击中陨石
    update_explosions()  # 更新爆炸效果
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
