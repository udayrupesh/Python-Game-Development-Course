score = 0

quiz = (
    ("1. Which footballer has won the World Cup 3 times?",
     ("Pele","Maradona","Cafu","Zidane"),
     1),
    ("2. How Many UCLS have Liverpool  won?",
     ("3","5","6","8"),
     3),
    ("3. How much does Yamal earn a year?",
     ("12M","25M","33M","37M"),
     3),
    ("4. How much Does an authentic 2006 France shirt cost?",
     ("£100","£350","£700","£1000"),
     2), 
    ("5.Which player has won the most Ballon Dors?",
     ("Ronaldo","Kaka","Platini","Messi"),
     4),
    ("6.What is the price to buy FC Barcelona?",
     ("2.7B","5.5B","7.5B","10B"),
     3),
    ("7.What was Zidanes number for Real Madrid?",
     ("5","10","20","80"),
     1),
    ("8.Where is Andre Onana From?",
     ("Senegal","Somalia","Chad","Cameroon"),
     4),
    ("9.Who won the Serie A in the 22/23 season?",
     ("Inter Milan","Napoli","Lazio","Juventus"),
     2),
    ("10.Who has played for both Real Madrid and FC Barcelona?",
     ("Xavi Hernandez","Carlos Puyol","Luis Figo","Luis Suarez"),
     3),


)

for question in quiz:
    print("\n" + question[0])

    print("1.", question[1][0])
    print("2.", question[1][1])
    print("3.", question[1][2])
    print("4.", question[1][3])

    answer = int(input("Enter your choice (1-4):"))

    if answer == question[2]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", question[1][question[2] - 1])

print("\n========== QUIZ COMPLETED ==========")
print("Your Final Score:" , score, "/10")

if score == 10:
    print("Excellent! Perfect Score!")
elif score >= 8:
    print("Great Job!")
elif score >= 5:
    print("Good Effort! Keep Practicing")
else:
    print("Practice More! You'll Improve.")