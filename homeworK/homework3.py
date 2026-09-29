import pgzrun


WIDTH = 800
HEIGHT = 400

def draw():
    screen.clear()
    screen.fill("white")

    x = 50

    while x < WIDTH:
        # Circle
        screen.draw.filled_circle((x, 200), 25, "red")

        # Square
        screen.draw.filled_rect(Rect((x + 50, 175), (50, 50)), "blue")

        x += 100

pgzrun.go()