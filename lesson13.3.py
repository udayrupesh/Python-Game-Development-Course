import random
words = [
    "Messi",
    "Ronaldo",
    "Mbappé",
    "Haaland",
    "Bellingham",
    "Neymar",
    "Salah",
    "Kane",
    "Vinícius",
    "De Bruyne",
    "Saka",
    "Foden",
    "Yamal",
    "Lewandowski",
    "Son",
    "Fernandes",
    "Palmer",
    "Van Dijk",
    "Rodri",
    "Griezmann",
    "Pedri",
    "Rice",
    "Ødegaard",
    "Suárez",
    "Ronaldinho",
    "Zidane",
    "Henry",
    "Beckham",
    "Rooney",
    "Nazário"
]
secret_footballer = set(random.sample(words, 5))

guessed_words = set()

attempts = 0

print("Welcome to Guess the Secret Set Of Footballers Game!")
print("I have selected 5 unique Footballers.")
print("Try to guess them\n")

while guessed_words != secret_footballer:

    guess = (input("Enter your guess:"))

    attempts += 1

    if guess in guessed_words:
        print("You already guessed this number!")

    elif guess in secret_footballer:
        print("Correct guess!")
        guessed_words.add(guess)

    else:
       print("Werong guess,try again!")

    print("Your correct guesses so far:", guessed_words)

    print()

print("Congratulations! You guessed all Footballers!")
print("Secret set was:", secret_footballler)

print("Total attempts:", attempts)
