import pgzrun

WIDTH = 600
HEIGHT = 300

message = "Press SPACE to check password"

def draw():
    screen.clear()
    screen.fill("white")
    screen.draw.text(message, center=(300, 150), color="black", fontsize=35)

def on_key_down(key):
    global message

    if key == keys.SPACE:
        password = input("Enter a password: ")

        unique_count = len(set(password))

        if len(password) >= 8 and unique_count >= 6:
            strength = "Strong"
        elif len(password) >= 6 and unique_count >= 4:
            strength = "Medium"
        else:
            strength = "Weak"

        message = f"Unique: {unique_count} | {strength}"

pgzrun.go()