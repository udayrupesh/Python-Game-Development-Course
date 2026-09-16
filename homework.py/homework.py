import pgzrun

WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()

    # Sky
    screen.fill((135, 206, 235))

    # Grass
    screen.draw.filled_rect(Rect((0, 450), (800, 150)), (34, 139, 34))

    # Sun
    screen.draw.filled_circle((100, 100), 60, (255, 255, 0))

    # Mountains
    screen.draw.filled_polygon([(200, 450), (350, 250), (500, 450)], (120, 120, 120))
    screen.draw.filled_polygon([(400, 450), (550, 300), (700, 450)], (100, 100, 100))

    # House base
    screen.draw.filled_rect(Rect((550, 380), (150, 120)), (178, 34, 34))

    # Roof
    screen.draw.filled_polygon([(550, 380), (625, 300), (700, 380)], (139, 69, 19))

    # Door
    screen.draw.filled_rect(Rect((610, 430), (40, 70)), (80, 40, 0))

    # Windows
    screen.draw.filled_rect(Rect((570, 410), (40, 40)), (173, 216, 230))
    screen.draw.filled_rect(Rect((640, 410), (40, 40)), (173, 216, 230))

pgzrun.go()
