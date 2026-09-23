import pgzrun

WIDTH = 800
HEIGHT = 500

# SUN POSITION
sun_x = 100
sun_y = 100

def draw():
    screen.clear()

    #SKY
    screen.fill("skyblue")

    #SUN
    screen.draw.filled_circle((sun_x,sun_y), 40, "yellow")

    #CLOUD 1
    screen.draw.filled_circle((180,120),25, "white")
    screen.draw.filled_circle((210,105),35, "white")
    screen.draw.filled_circle((245,120),25, "white")
    screen.draw.filled_rect(Rect((175,120), (75,25)), "white")

    #CLOUD 2
    screen.draw.filled_circle((500,180),25, "white")
    screen.draw.filled_circle((535,160),35, "white")
    screen.draw.filled_circle((570,180),25, "white")
    screen.draw.filled_rect(Rect((495,180), (80,25)), "white")

    screen.draw.filled_rect(Rect((0,400), (8000,100)), "green")

def update():
    global sun_x
    sun_x = sun_x + 1
    if sun_x > WIDTH + 40:
        sun_x = -40
pgzrun.go()