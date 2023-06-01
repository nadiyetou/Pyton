# Sample data dictionary.
sample_data = {
    "One Piece": {
        "synopsis": "Gol D. Roger was known as the Pirate King...",
        "episodes": 1000,
        "rating": 8.56
    },
    "Naruto": {
        "synopsis": "Naruto Uzumaki, a mischievous adolescent ninja...",
        "episodes": 720,
        "rating": 8.19
    },
    "Attack on Titan": {
        "synopsis": "Several hundred years ago, humans were nearly exterminated by Titans...",
        "episodes": 75,
        "rating": 8.49
    },
    "Death Note": {
        "synopsis": "Light Yagami, an intelligent high school student...",
        "episodes": 37,
        "rating": 8.66
    },
    "Fullmetal Alchemist: Brotherhood": {
        "synopsis": "Edward and Alphonse Elric's reckless pursuit of...",
        "episodes": 64,
        "rating": 9.22
    },
    "Dragon Ball Z": {
        "synopsis": "Goku and his friends defend the Earth against villains...",
        "episodes": 291,
        "rating": 8.31
    },
    "Bleach": {
        "synopsis": "Ichigo Kurosaki gains the abilities of a Soul Reaper...",
        "episodes": 366,
        "rating": 7.92
    },
    "My Hero Academia": {
        "synopsis": "In a world where most of the population has superpowers...",
        "episodes": 113,
        "rating": 8.24
    }
    # Add more anime entries here
}

# Function to get anime information
def get_anime_info(anime_name):
    if anime_name in sample_data:
        anime = sample_data[anime_name]
        title = anime_name
        synopsis = anime["synopsis"]
        episodes = anime["episodes"]
        rating = anime["rating"]

        # Printing the information
        print("Title:", title)
        print("Synopsis:", synopsis)
        print("Episodes:", episodes)
        print("Rating:", rating)
    else:
        print("No anime found with that name.")

# Main program
def main():
    while True:
        print("==== Anime Information App ====")
        print("Enter the name of an anime (or 'q' to quit):")
        anime_name = input("> ")

        if anime_name == "q":
            break

        get_anime_info(anime_name)
        print()

# Calling the main program
main()
