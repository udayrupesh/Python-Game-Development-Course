


spaceship = (0, 0)


stars = [(2, 1), (4, 3), (1, 4)]

score = 0

print("🚀 SPACE STAR CATCHER 🚀")
print("Collect all the glowing stars!")
print("W = Up, S = Down, A = Left, D = Right")

while len(stars) > 0:

    
    print("\n" + "=" * 20)

    for y in range(4, -1, -1):
        for x in range(5):
            pos = (x, y)

            if pos == spaceship:
                print("🚀", end=" ")
            elif pos in stars:
                print("⭐", end=" ")
            else:
                print("⬜", end=" ")
        print()

    print("\nStars Collected:", score)

    move = input("\nMove: ").lower()

    x, y = spaceship

    if move == "w" and y < 4:
        spaceship = (x, y + 1)

    elif move == "s" and y > 0:
        spaceship = (x, y - 1)

    elif move == "a" and x > 0:
        spaceship = (x - 1, y)

    elif move == "d" and x < 4:
        spaceship = (x + 1, y)

    
    if spaceship in stars:
        stars.remove(spaceship)
        score += 1
        print("✨ Star Collected! ✨")

print("\n🎉 CONGRATULATIONS! 🎉")
print("You collected all the stars!")
print("Final Score:", score)