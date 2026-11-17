import random
import pgzrun

WIDTH = 800
HEIGHT = 600

score = 0
game_over = False

healthy_foods = ["apple", "banana", "carrot"]
junk_foods = ["burger", "pizza", "donut"]

current_food = Actor(random.choice(healthy_foods + junk_foods))
current_food.pos = (400, 300)


def draw():
    screen.clear()
    screen.fill("lightblue")

    if game_over:
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=60,
            color="red"
        )
        screen.draw.text(
            f"Final Score: {score}",
            center=(WIDTH // 2, HEIGHT // 2 + 60),
            fontsize=40,
            color="black"
        )
    else:
        current_food.draw()

        screen.draw.text(
            f"Score: {score}",
            topleft=(10, 10),
            fontsize=40,
            color="black"
        )


def on_mouse_down(pos):
    global score, game_over

    if game_over:
        return

    if current_food.collidepoint(pos):

        if current_food.image in healthy_foods:
            score += 1
            move_food()

        elif current_food.image in junk_foods:
            game_over = True


def move_food():
    current_food.image = random.choice(healthy_foods + junk_foods)
    current_food.x = random.randint(50, WIDTH - 50)
    current_food.y = random.randint(50, HEIGHT - 50)

pgzrun.go()