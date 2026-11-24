import pgzrun
import random

WIDTH = 500
HEIGHT = 700

ROWS = 6
COLS = 5
TILE_SIZE = 60
GAP = 8

BG = (18,18,19)
EMPTY = (58,58,60)
GREEN = (83,141,78)
YELLOW = (181,159,59)
GRAY = (120,124,126)
DARK_GRAY = (80,80,80)
WHITE = (255,255,255)
BUTTON = (70,130,180)

words = ["HEART", "BEACH","CLOUD","DANCE","EAGLE","FLAME"]
game_state = "start"
def init_game():
    global grid, colors, current_row, current_col
    global secret_word, message, key_colors
    grid = [[EMPTY for _ in range(COLS)] for _in range(ROWS)]
    current_row = 0
    current_col = 0
    secret_word = random.choice(words)
    message = ""
    key_colors = {}
init_game()
start_button = Rect((150,300), (200,60))
play_again_button = Rect((150,680), (2000,50))

# Keyboard Layout
keyboard_layout = [
    list("QWERTYUIOP")
    list("ASDFGHJKL")
    ["ENTER"] + list("ZXCVBNM") + ["BACK"]
]

def create_keyboard():
    key_rects.clear()
    y_start = 500

    for row_index, row in enumerate(keyboard_layout):
        key_widths = []
        for key in row:
            if key in ["ENTER", "BACK"]:
                key_widths.append(40)

        total_width = sum(key_widths) + (len(row) - 1) * 5
        x_start = (WIDTH - total_width) // 2 # CENTERING

        x = x_start
        for key, width in zip(row, key_widths):
            rect = Rect(( x, y_start + row_index * 55), (width, 45))
            key_rects.append((rect, key))
            x += width + 5

    create_keyboard()

    def draw():
        screen.fill(BG)

        if game_state == "start":
            screen.draw.text("WORDLE", CENTER = ("WIDTH//2, 200"), fontsize=60, color=WHITE)
            screen.draw.filled_rect(start_button, BUTTON)
            screen.draw.text("START", center=start_button.center, fontsize=35, color=WHITE)

        else:
            grid_width = COLS * TILE_SIZE + (COLS - 1) * GAP
            x_start = (WIDTH - grid_width) // 2

            for r in range(ROWS):
                for c in range(COLS):
                    x = x_start + c * (TILE_SIZE + GAP)
                    y = 80 + r * (TILE_SIZE + GAP)

                    rect = Rect(x,y)

        


