# This is a list of dictionaries where each dictionary represents an anime and its details.
anime_list = [
    {"name": "Naruto", 
     "genre": "Action, Adventure, Fantasy", 
     "episodes": 220,
     "summary": "Naruto follows the journey of Naruto Uzumaki, a young ninja who seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village."},
    
    {"name": "Death Note", 
     "genre": "Mystery, Psychological thriller", 
     "episodes": 37,
     "summary": "Death Note is about a high school student who discovers a supernatural notebook that allows him to kill anyone by writing the victim's name while picturing their face. The story follows his attempts to become a god by creating a New World cleansed of evil, using the notebook."},
    
    {"name": "Attack on Titan", 
     "genre": "Action, Post-apocalyptic", 
     "episodes": 75,
     "summary": "In a world where humanity is threatened by gigantic humanoid creatures known as Titans, a young man named Eren Yeager joins the military with his friends to fight for survival."},
     
    {"name": "One Piece", 
     "genre": "Adventure, Fantasy", 
     "episodes": 1000,
     "summary": "One Piece follows the adventures of Monkey D. Luffy and his pirate crew in order to find the greatest treasure ever left by the legendary Pirate, Gold Roger. The famous mystery treasure named 'One Piece'."},
     
    {"name": "Fullmetal Alchemist: Brotherhood", 
     "genre": "Action, Adventure, Dark fantasy", 
     "episodes": 64,
     "summary": "The story of two brothers, Edward and Alphonse Elric, who are searching for a Philosopher's Stone to restore their bodies after a failed attempt to bring their mother back to life using Alchemy."}
]

# Function to search for anime in the list and print its details.
def search_anime(anime_name):
    # Loop through each anime in the list.
    for anime in anime_list:
        # Check if the name of the anime matches the name entered by the user.
        if anime["name"].lower() == anime_name.lower():
            # If a match is found, print the details of the anime and return from the function.
            print(f"\nAnime name: {anime['name']}\nGenre: {anime['genre']}\nNumber of episodes: {anime['episodes']}\nSummary: {anime['summary']}\n")
            return

    # If no match is found, print a message indicating that the anime was not found.
    print(f"\nNo anime found with the name: {anime_name}\n")

print(""" $$$$$$\            $$\                               $$\   $$\                 $$\ $$\           
$$  __$$\           \__|                              $$$\  $$ |                $$ |\__|          
$$ /  $$ |$$$$$$$\  $$\ $$$$$$\$$$$\   $$$$$$\        $$$$\ $$ | $$$$$$\   $$$$$$$ |$$\  $$$$$$\  
$$$$$$$$ |$$  __$$\ $$ |$$  _$$  _$$\ $$  __$$\       $$ $$\$$ | \____$$\ $$  __$$ |$$ | \____$$\ 
$$  __$$ |$$ |  $$ |$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ \$$$$ | $$$$$$$ |$$ /  $$ |$$ | $$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ |$$ | $$ | $$ |$$   ____|      $$ |\$$$ |$$  __$$ |$$ |  $$ |$$ |$$  __$$ |
$$ |  $$ |$$ |  $$ |$$ |$$ | $$ | $$ |\$$$$$$$\       $$ | \$$ |\$$$$$$$ |\$$$$$$$ |$$ |\$$$$$$$ |
\__|  \__|\__|  \__|\__|\__| \__| \__| \_______|      \__|  \__| \_______| \_______|\__| \_______|""")

print("Anime")
print("\nKonichiwa! Welcome to AnimeFinder, where you get info about your favorite animes. Let's start the journey...\n")

# Repeat this block until the user wants to quit.
while True:
    # Prompt the user to enter the name of an anime.
    anime_name = input("Enter the name of an anime: ")

    # Call the search_anime function with the name entered by the user.
    search_anime(anime_name)

    # Ask the user if they want to continue or quit the program.
    continue_choice = input("Would you like to search for another anime? (yes/no): ")
    if continue_choice.lower() != 'yes':
        break

print("""
 /\_/\  
( o.o ) 
 > ^ <  
 /\_/\  
( o.o ) 
 > ^ <  
""")
print("Arigato for using AnimeFinder! Hope you had a fantastic anime journey. Sayonara and see you next time!")
