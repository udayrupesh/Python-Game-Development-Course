import pgzrun

WIDTH = 500
HEIGHT= 500
def draw():
    
    screen.clear()
    screen.fill("white")
    screen.draw.filled_circle((250,250), 150, "yellow")

    screen.draw.filled_circle((200,210), 15, "black")
    screen.draw.filled_circle((300,210), 15, "black")

    screen.draw.line((190,290), (215,310), "black",)
    screen.draw.line((215,310), (250,320), "black",)
    screen.draw.line((250,320), (285,310), "black",)
    screen.draw.line((285,310), (310,290),"black",)

pgzrun.go()


