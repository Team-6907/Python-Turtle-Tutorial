# ======================
# 🎁 Bonus: 射击功能
# ======================
# 学习目标：
# - 创建子弹系统
# - 实现子弹与陨石的碰撞检测
# - 按空格键发射子弹
# - 综合运用之前学到的所有知识
#
# 💪 这是挑战关卡！需要综合运用之前学的所有知识

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
# 飞船移动
# ======================


def move_left():
    if player.xcor() > -380:
        player.setx(player.xcor() - 20)


def move_right():
    if player.xcor() < 380:
        player.setx(player.xcor() + 20)


def move_up():
    if player.ycor() < 200:
        player.sety(player.ycor() + 20)


def move_down():
    if player.ycor() > -280:
        player.sety(player.ycor() - 20)


# ======================
# 任务1：创建子弹系统
# ======================

# TODO: 创建一个空列表来存储子弹（和陨石一样的思路）
bullets = ______


def create_bullet():
    """创建一颗新子弹"""
    bullet = turtle.Turtle()

    # TODO: 设置子弹形状为 "square"
    bullet.shape(______)

    # TODO: 设置子弹颜色为黄色 "#ffff00"
    bullet.color(______)

    bullet.shapesize(0.2, 0.5)  # 细长的形状
    bullet.penup()
    bullet.setheading(90)  # 朝向上方

    # TODO: 设置子弹初始位置 = 飞船位置上方
    # 提示：使用 player.xcor() 和 player.ycor() + 20
    bullet.setposition(player.______(), player.______() + 20)

    # TODO: 把子弹添加到 bullets 列表
    bullets.______(bullet)


def shoot():
    """发射子弹（带冷却时间）"""
    global last_shot_time

    current_time = time.time()

    # TODO: 检查冷却时间是否已过
    # 如果 current_time - last_shot_time >= shoot_cooldown
    if current_time - last_shot_time >= ______:
        create_bullet()
        last_shot_time = current_time


# ======================
# 任务2：移动子弹
# ======================


def move_bullets():
    """移动所有子弹"""
    # 使用 bullets[:] 创建列表副本，避免遍历时修改原列表
    for bullet in bullets[:]:
        y = bullet.ycor()

        # TODO: 子弹向上移动，速度为 15
        y += ______

        bullet.sety(y)

        # TODO: 如果子弹超出屏幕顶部（y > 310），移除子弹
        if y > ______:
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
# 任务3：子弹击中陨石检测
# ======================


def check_bullet_hit():
    """检测子弹是否击中陨石"""
    global score

    # 遍历所有子弹
    for bullet in bullets[:]:
        # 遍历所有陨石
        for asteroid in asteroids:
            # TODO: 计算子弹和陨石的距离
            # 如果距离 < 20，表示击中
            if bullet.______(asteroid) < ______:
                # 击中了！

                # TODO: 分数增加 5 分
                score += ______

                # 移除子弹
                bullet.hideturtle()
                bullets.remove(bullet)

                # 重置陨石到顶部
                reset_asteroid(asteroid)

                # 创建爆炸效果
                create_explosion(asteroid.xcor(), asteroid.ycor())

                break  # 一颗子弹只能击中一个陨石


# ======================
# 爆炸效果（已完成）
# ======================

explosions = []


def create_explosion(x, y):
    """在指定位置创建爆炸效果"""
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
# 飞船与陨石碰撞检测（已完成）
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
# 任务4：绑定空格键
# ======================

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")

# TODO: 绑定空格键到 shoot 函数
screen.onkeypress(______, "space")

# ======================
# 任务5：更新游戏主循环
# ======================

while not game_over:
    move_asteroids()

    # TODO: 调用移动子弹函数
    ______()

    # TODO: 调用检测子弹击中函数
    ______()

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
# 🎯 完成后的挑战
# ======================
# 1. 修改 shoot_cooldown 的值，让射击更快或更慢
# 2. 修改击中陨石的得分，从 5 分改成 10 分
# 3. 修改子弹颜色和速度
# 4. 【高级】添加子弹数量限制（屏幕上最多5颗子弹）
