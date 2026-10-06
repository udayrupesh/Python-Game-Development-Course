import pgzrun

WIDTH = 800
HEIGHT = 600

ball = Actor("mbappe")
ball.pos = (100, 500)

hoop = Actor("imagemiem")
hoop.pos = (700, 250)

score = 0

ball_vx = 0
ball_vy = 0
shot = False


def draw():
    screen.clear()
    screen.fill((135, 206, 235))

    ball.draw()
    hoop.draw()

    screen.draw.text(
        "Score: " + str(score),
        (20, 20),
        color="black",
        fontsize=40
    )


def on_mouse_down(pos):
    global ball_vx, ball_vy, shot

    if not shot:
        dx = pos[0] - ball.x
        dy = pos[1] - ball.y

        ball_vx = dx / 20
        ball_vy = dy / 20

        shot = True


def update():
    global ball_vx, ball_vy, shot, score

    if shot:
        ball.x += ball_vx
        ball.y += ball_vy

        # Gravity
        ball_vy += 0.4

        # Score if ball touches hoop
        if ball.colliderect(hoop):
            score += 1
            reset_ball()

        # Missed shot
        if ball.y > HEIGHT or ball.x > WIDTH:
            reset_ball()


def reset_ball():
    global shot, ball_vx, ball_vy

    ball.pos = (100, 500)
    ball_vx = 0
    ball_vy = 0
    shot = False

pgzrun.go()
