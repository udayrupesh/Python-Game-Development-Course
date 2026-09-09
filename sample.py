

music = {
    "Shake It Off": {"Singer": "Taylor Swift", "Genre": "Pop", "Rating": 9.8},
    "Blinding Lights": {"Singer": "The Weeknd", "Genre": "Synthwave", "Rating": 9.7},
    "Bad Guy": {"Singer": "Billie Eilish", "Genre": "Pop", "Rating": 9.2},
    "Uptown Funk": {"Singer": "Bruno Mars", "Genre": "Funk", "Rating": 9.5},
    "Shape of You": {"Singer": "Ed Sheeran", "Genre": "Pop", "Rating": 9.3},
    "Humble": {"Singer": "Kendrick Lamar", "Genre": "Rap", "Rating": 9.6}
}

while True:
    print("========= Favorite Songs =========")
    print("1. View All Songs")
    print("2. Search a Song")
    print("3. Update Song Rating")
    print("4. Add a New Song")
    print("5. Exit")
    print("==================================")

    choice = input("Enter your choice: ")


    if choice == "1":
        for title, info in music.items():
            print(f"\nTitle: {title}")
            print(f" Singer: {info['Singer']}")
            print(f" Genre: {info['Genre']}")
            print(f" Rating: {info['Rating']}")

    
    elif choice == "2":
        name = input("Enter song name: ")
        if name in music:
            print(f"\nTitle: {name}")
            print(f" Singer: {music[name]['Singer']}")
            print(f" Genre: {music[name]['Genre']}")
            print(f" Rating: {music[name]['Rating']}")
        else:
            print("Song not found.")

    
    elif choice == "3":
        name = input("Enter song name to update: ")
        if name in music:
            new_rating = float(input("Enter new rating: "))
            music[name]["Rating"] = new_rating
            print("Rating updated!")
        else:
            print("Song not found.")

    
    elif choice == "4":
        title = input("Enter song title: ")
        singer = input("Enter singer: ")
        genre = input("Enter genre: ")
        rating = float(input("Enter rating: "))
        music[title] = {"Singer": singer, "Genre": genre, "Rating": rating}
        print("Song added!")

    
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


