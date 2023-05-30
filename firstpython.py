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
    anime_name = input("Enter the name of the anime: ")

    # Calling the function to get anime information
    get_anime_info(anime_name)

# Calling the main program
main()
