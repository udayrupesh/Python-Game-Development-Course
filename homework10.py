
import pgzrun

# Game settings
WIDTH = 480
HEIGHT = 480
CELL_SIZE = 80
ROWS = 6
COLS = 6

# Game map: . = path, X = obstacle, C = coin, T = treasure
grid = [
    [".", ".", "X", ".", "C", "."],
    [".", "X", ".", ".", "X", "."],
    ["C", ".", ".", "X", ".", "."],
    [".", ".", "X", ".", ".", "C"],
    ["X", ".", ".", ".", "X", "."],
    [".", "C", ".", ".", ".", "T"]
]

# Player starting position
player_row = 0
player_col = 0
score = 0
game_won = False


def draw():
    screen.clear()
    screen.fill("lightblue")

    # Display the grid using nested for loops
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if grid[row][col] == "X":
                colour = "darkgray"
            elif grid[row][col] == "C":
                colour = "gold"
            elif grid[row][col] == "T":
                colour = "green"
            else:
                colour = "white"

            screen.draw.filled_rect(
                Rect(x, y, CELL_SIZE, CELL_SIZE), colour
            )
            screen.draw.rect(
                Rect(x, y, CELL_SIZE, CELL_SIZE), "black"
            )

            # Display coins and treasure
            if grid[row][col] == "C":
                screen.draw.text(
                    "C", center=(x + 40, y + 40),
                    fontsize=40, color="black"
                )
            elif grid[row][col] == "T":
                screen.draw.text(
                    "T", center=(x + 40, y + 40),
                    fontsize=40, color="white"
                )
            elif grid[row][col] == "X":
                screen.draw.text(
                    "X", center=(x + 40, y + 40),
                    fontsize=40, color="white"
                )

    # Draw the player
    px = player_col * CELL_SIZE + CELL_SIZE // 2
    py = player_row * CELL_SIZE + CELL_SIZE // 2
    screen.draw.filled_circle((px, py), 20, "blue")

    # Display score
    screen.draw.text(
        "Score: " + str(score),
        topleft=(5, 5), color="red", fontsize=25
    )

    if game_won:
        screen.draw.text(
            "YOU WIN!",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=60, color="red"
        )


def on_key_down(key):
    global player_row, player_col, score, game_won

    if game_won:
        return

    new_row = player_row
    new_col = player_col

    # Move using arrow keys
    if key == keys.UP:
        new_row -= 1
    elif key == keys.DOWN:
        new_row += 1
    elif key == keys.LEFT:
        new_col -= 1
    elif key == keys.RIGHT:
        new_col += 1
    else:
        return

    # Prevent moving outside the grid
    if new_row < 0 or new_row >= ROWS:
        return
    if new_col < 0 or new_col >= COLS:
        return

    # Prevent moving onto obstacles
    if grid[new_row][new_col] == "X":
        return

    # Update player position
    player_row = new_row
    player_col = new_col

    # Collect coins
    if grid[player_row][player_col] == "C":
        score += 1
        grid[player_row][player_col] = "."

    # Check for treasure
    if grid[player_row][player_col] == "T":
        game_won = True


pgzrun.go()
