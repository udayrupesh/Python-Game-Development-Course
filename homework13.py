
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Create the spaceship
spaceship = Actor("spaceship")
spaceship.pos = (400, 500)

# Create a list of stars
stars = []

# Add 5 stars
for i in range(5):
    star = Actor("star")
    star.pos = (
        random.randint(50, 750),
        random.randint(50, 400)
    )
    stars.append(star)

score = 0
speed = 5


def update():

    global score

    # Move spaceship
    if keyboard.left:
        spaceship.x -= speed

    if keyboard.right:
        spaceship.x += speed

    if keyboard.up:
        spaceship.y -= speed

    if keyboard.down:
        spaceship.y += speed

    # Keep spaceship inside screen
    if spaceship.x < 30:
        spaceship.x = 30

    if spaceship.x > WIDTH - 30:
        spaceship.x = WIDTH - 30

    if spaceship.y < 30:
        spaceship.y = 30

    if spaceship.y > HEIGHT - 30:
        spaceship.y = HEIGHT - 30

    # Check star collection
    for star in stars[:]:

        if spaceship.colliderect(star):

            stars.remove(star)
            score += 1

            # Create a new star
            new_star = Actor("star")
            new_star.pos = (
                random.randint(50, 750),
                random.randint(50, 400)
            )

            stars.append(new_star)


def draw():

    screen.blit("space", (0, 0))

    # Draw spaceship
    spaceship.draw()

    # Draw all stars
    for star in stars:
        star.draw()

    # Display score
    screen.draw.text(
        "Score: " + str(score),
        (20, 20),
        color="yellow",
        fontsize=40
    )


pgzrun.go()

