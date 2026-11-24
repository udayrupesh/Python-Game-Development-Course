print("🎉 Welcome to the Fun Riddles Quiz! 🎉")

score = 0

answer = input("1. What has keys but can't open locks? ").lower()
if answer == "piano":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Piano.")

answer = input("2. What has hands but cannot clap? ").lower()
if answer == "clock":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Clock.")

answer = input("3. What has a face and two hands but no arms or legs? ").lower()
if answer == "clock":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Clock.")

answer = input("4. What gets wetter as it dries? ").lower()
if answer == "towel":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Towel.")

answer = input("5. What has one eye but cannot see? ").lower()
if answer == "needle":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Needle.")

print("\nQuiz Finished!")
print("Your score is", score, "out of 5")