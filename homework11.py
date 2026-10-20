import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    ctypes.windll.user32.SetProcessDPIAware()

import pgzrun
import random



WIDTH = 500
HEIGHT = 500
TITLE = "Collect the Apples"



basket = Actor("basket")
basket.x = WIDTH // 2
basket.y = HEIGHT - 60

apple = Actor("apple")
apple.x = random.randint(30, WIDTH - 30)
apple.y = 0


basket_speed = 5
apple_speed = 3
score = 0


def draw():
    screen.clear()

    
    screen.blit("background", (0, 0))

    apple.draw()
    basket.draw()

    
    screen.draw.text(
        "Score: " + str(score),
        (20, 20),
        color="black",
        fontsize=35
    )


def update():
    global score


    if keyboard.left or keyboard.a:
        basket.x -= basket_speed

    
    if keyboard.right or keyboard.d:
        basket.x += basket_speed

    
    if basket.left < 0:
        basket.left = 0

    if basket.right > WIDTH:
        basket.right = WIDTH

    
    apple.y += apple_speed

    if basket.colliderect(apple):
        score += 1
        reset_apple()

    
    elif apple.top > HEIGHT:
        reset_apple()


def reset_apple():
    apple.x = random.randint(30, WIDTH - 30)
    apple.y = 0

pgzrun.go()