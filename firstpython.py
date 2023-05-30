# Function to get anime information from sample data
def get_anime_info(anime_name):
    # Sample data dictionary
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
        },
        "Hunter x Hunter": {
            "synopsis": "Gon Freecss aspires to become a Hunter, an exceptional being...",
            "episodes": 148,
            "rating": 9.09
        },
        "Demon Slayer": {
            "synopsis": "Tanjiro Kamado becomes a demon slayer after his family...",
            "episodes": 26,
            "rating": 8.75
        },
        "Fairy Tail": {
            "synopsis": "Lucy Heartfilia joins the Fairy Tail wizard guild...",
            "episodes": 328,
            "rating": 8.15
        },
        "Sword Art Online": {
            "synopsis": "In the year 2022, virtual reality MMORPG...",
            "episodes": 97,
            "rating": 7.53
        },
        "One Punch Man": {
            "synopsis": "Saitama, a hero who can defeat any opponent with a single punch...",
            "episodes": 24,
            "rating": 8.58
        }
    }

    # Check if anime exists in the sample data
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
    # Getting anime name from the user
    anime_name =input("Enter the name of the anime: ")

    # Calling the function to get anime information
    get_anime_info(anime_name)

# Calling the main program
main()
