import pgzrun
from random import randint

TITLE = "Good Shot Game"
WIDTH = 500
HEIGHT = 500

message = ""
score = 0
game_over = False

alien = Actor("imagemiem")

def draw():
    screen.clear()
    screen.fill((128,0,0))

    if game_over:
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2 ),
            fontsize=60,
            color= "white"
        )
        screen.draw.text(
            f"Final Score: {score}",
            center=(WIDTH // 2, HEIGHT // 2+50),
            fontsize=40,
            color="white"
        )
    else:
        alien.draw()
        screen.draw.text(
            message,
            center=(400,20),
            fontsize=30,
            color="white"
        )
        screen.draw.text(
            f"Score: {score}",
            topleft=(10,10),
            fontsize=30,
            color="white"
        )

def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)

def end_game():
    quit()

def on_mouse_down(pos):
    global message,score,game_over

    if game_over:
        return

    if alien.collidepoint(pos):
        message = "Good Shot!"
        score += 1
        place_alien()
    else:
        message = "You Missed!"
        game_over = True
        clock.schedule_unique(end_game,2)

place_alien()
pgzrun.go()  

        
