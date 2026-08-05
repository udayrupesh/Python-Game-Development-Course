

movies = {
    "Inception": {
        "Director": "Christopher Nolan",
        "Year": 2010,
        "Rating": 8.8
    },
    "Interstellar": {
        "Director": "Christopher Nolan",
        "Year": 2014,
        "Rating": 8.6
    },
    "The Matrix": {
        "Director": "The Wachowskis",
        "Year": 1999,
        "Rating": 8.7
    }
}

def view_all_movies():
    print("\n=== All Movies ===")
    for name, info in movies.items():
        print(f"\nMovie: {name}")
        print(f" Director: {info['Director']}")
        print(f" Year: {info['Year']}")
        print(f" Rating: {info['Rating']}")
    print("====================\n")

def search_movie():
    name = input("Enter movie name to search: ")
    if name in movies:
        print("\nMovie Found!")
        print(f" Director: {movies[name]['Director']}")
        print(f" Year: {movies[name]['Year']}")
        print(f"Rating: {movies[name]['Rating']}\n")
    else:
        print("Movie not found.\n")

def update_rating():
    name = input("Enter movie name to update rating: ")
    if name in movies:
        new_rating = float(input("Enter new rating: "))
        movies[name]["Rating"] = new_rating
        print("Rating updated successfully!\n")
    else:
        print("Movie not found.\n")

def add_movie():
    name = input("Enter new movie name: ")
    director = input("Enter director: ")
    year = int(input("Enter release year: "))
    rating = float(input("Enter rating: "))

    movies[name] = {
        "Director": director,
        "Year": year,
        "Rating": rating
    }

    print("Movie added successfully!\n")

while True:
    print("========== Favorite Movies ==========")
    print("1. View All Movies")
    print("2. Search a Movie")
    print("3. Update Movie Rating")
    print("4. Add a New Movie")
    print("5. Exit")
    print("====================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all_movies()
    elif choice == "2":
        search_movie()
    elif choice == "3":
        update_rating()
    elif choice == "4":
        add_movie()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
