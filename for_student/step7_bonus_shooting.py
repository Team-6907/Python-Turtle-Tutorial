# ======================
# 🎁 Bonus: 射击 + 平滑移动
# ======================
# 这是给进度快的同学的挑战！
#
# 【你将学到的新概念】
#
# 一、平滑移动系统
#    - 速度 (velocity) - 物体移动的快慢和方向
#    - 加速度 (acceleration) - 按键时速度增加
#    - 摩擦力 (friction) - 松开按键后速度逐渐减小
#    - onkeyrelease - 检测按键松开
#
# 二、射击系统
#    - 冷却时间 (cooldown) - 防止连续射击太快
#    - 列表切片 bullets[:] - 安全地遍历并修改列表
#
# 【设计动机】
#
# Q: 为什么要平滑移动？之前的移动方式有什么问题？
# A: 之前按一下移动20像素，手感生硬。平滑移动有加速和惯性，更像真实飞船。
#
# Q: 摩擦力是怎么实现的？
# A: 每帧把速度乘以一个小于1的数（如0.85），速度就会逐渐变小。
#
# Q: 为什么需要 onkeyrelease？
# A: 要知道玩家什么时候松开按键，才能停止加速、让摩擦力生效。
#
# Q: 为什么需要冷却时间？
# A: 没有冷却，按住空格瞬间发射几十颗子弹，游戏太简单且卡顿。

import turtle
import random
import time

# ======================
# 游戏配置
# ======================

score = 0
game_over = False
last_score_time = time.time()

# 射击配置
last_shot_time = 0
shoot_cooldown = 0.3  # 射击冷却 0.3 秒

# ======================
# 【新概念】平滑移动配置
# ======================
# 传统移动：按一下 → 瞬间移动固定距离
# 平滑移动：按住 → 加速，松开 → 摩擦减速

keys_pressed = set()  # 存储当前按下的键（用集合避免重复）

player_vx = 0  # 水平速度 (velocity x)
player_vy = 0  # 垂直速度 (velocity y)

acceleration = 1.2  # 加速度：按键时每帧增加的速度
friction = 0.85  # 摩擦系数：每帧速度乘以这个数（<1 所以会减小）
max_speed = 12  # 最大速度：防止飞船飞太快

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
# 【任务1】平滑移动系统
# ======================


def key_press(key):
    """按键按下时，把键名加入集合"""
    keys_pressed.add(key)


def key_release(key):
    """按键松开时，把键名从集合移除"""
    keys_pressed.discard(key)  # discard 不会报错（即使 key 不存在）


def update_player_movement():
    """
    每帧调用，根据按键状态更新飞船速度和位置

    【物理原理】
    1. 按键 → 加速（速度增加）
    2. 松开 → 摩擦（速度乘以 <1 的数，逐渐减小）
    3. 速度 → 位置（位置 += 速度）
    """
    global player_vx, player_vy

    # TODO: 根据按键加速
    # 如果 "Left" 在 keys_pressed 中，水平速度减小
    if "Left" in keys_pressed or "a" in keys_pressed:
        player_vx -= ______  # 填 acceleration

    # TODO: 右移加速
    if "Right" in keys_pressed or "d" in keys_pressed:
        player_vx += ______

    # TODO: 上移加速
    if "Up" in keys_pressed or "w" in keys_pressed:
        player_vy += ______

    # TODO: 下移加速
    if "Down" in keys_pressed or "s" in keys_pressed:
        player_vy -= ______

    # 限制最大速度
    player_vx = max(-max_speed, min(max_speed, player_vx))
    player_vy = max(-max_speed, min(max_speed, player_vy))

    # TODO: 应用摩擦力（速度乘以 friction）
    player_vx *= ______
    player_vy *= ______

    # 速度很小时归零（防止无限滑动）
    if abs(player_vx) < 0.1:
        player_vx = 0
    if abs(player_vy) < 0.1:
        player_vy = 0

    # 计算新位置
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
        player_vy = 0


# ======================
# 【任务2】子弹系统
# ======================

bullets = []


def create_bullet():
    """创建一颗子弹"""
    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("#ffff00")
    bullet.shapesize(0.2, 0.5)
    bullet.penup()
    bullet.setheading(90)
    bullet.setposition(player.xcor(), player.ycor() + 20)
    bullets.append(bullet)


def shoot():
    """发射子弹（带冷却时间）"""
    global last_shot_time

    current_time = time.time()
    if current_time - last_shot_time >= shoot_cooldown:
        create_bullet()
        last_shot_time = current_time


def move_bullets():
    """移动所有子弹"""
    for bullet in bullets[:]:  # [:] 创建副本，安全遍历
        y = bullet.ycor()
        y += 15
        bullet.sety(y)

        if y > 310:
            bullet.hideturtle()
            bullets.remove(bullet)


# ======================
# 陨石系统（已完成）
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
# 【任务3】子弹击中检测
# ======================


def check_bullet_hit():
    """检测子弹击中陨石"""
    global score

    for bullet in bullets[:]:
        for asteroid in asteroids:
            # TODO: 距离 < 20 表示击中
            if bullet.distance(asteroid) < ______:
                score += 5
                bullet.hideturtle()
                bullets.remove(bullet)
                reset_asteroid(asteroid)
                create_explosion(asteroid.xcor(), asteroid.ycor())
                break


# ======================
# 爆炸效果（已完成）
# ======================

explosions = []


def create_explosion(x, y):
    exp = turtle.Turtle()
    exp.hideturtle()
    exp.penup()
    exp.setposition(x, y)
    exp.timer = 5
    explosions.append(exp)


def update_explosions():
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
# 碰撞检测（已完成）
# ======================


def check_player_collision():
    for asteroid in asteroids:
        if player.distance(asteroid) < 25:
            return True
    return False


# ======================
# UI显示（已完成）
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
tip_display.write("WASD/方向键移动 空格射击", font=("Courier", 12, "bold"))


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
# 游戏结束（已完成）
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
# 【任务4】键盘绑定
# ======================
# 平滑移动需要同时绑定 onkeypress 和 onkeyrelease

screen.listen()

# TODO: 方向键 - 按下时调用 key_press
screen.onkeypress(lambda: key_press("Left"), "Left")
screen.onkeypress(lambda: key_press("Right"), "Right")
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")

# WASD键 - 按下
screen.onkeypress(lambda: key_press("a"), "a")
screen.onkeypress(lambda: key_press("d"), "d")
screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")

# TODO: 方向键 - 松开时调用 key_release
screen.onkeyrelease(lambda: key_release("Left"), "Left")
screen.onkeyrelease(lambda: key_release("______"), "Right")  # 填 Right
screen.onkeyrelease(lambda: key_release("______"), "Up")  # 填 Up
screen.onkeyrelease(lambda: key_release("______"), "Down")  # 填 Down

# WASD键 - 松开
screen.onkeyrelease(lambda: key_release("a"), "a")
screen.onkeyrelease(lambda: key_release("d"), "d")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeyrelease(lambda: key_release("s"), "s")

# 射击
screen.onkeypress(shoot, "space")

# ======================
# 【任务5】游戏主循环
# ======================

while not game_over:
    # TODO: 调用平滑移动更新函数
    update_player_______()

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


# ======================
# 🎯 完成后的额外挑战
# ======================
# 1. 修改 acceleration = 2.0，体验更灵敏的操控
# 2. 修改 friction = 0.95，体验更长的滑行距离
# 3. 修改 max_speed = 20，体验极速飞船
# 4. 修改 shoot_cooldown = 0.2，体验更快的射击速度
# 5. 添加子弹数量限制
