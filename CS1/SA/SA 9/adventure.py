# File Name: adventure.py
# Author: Amittai Joel Wekesa
# Date: November 07, 2020
# Purpose: Adventure!!

# Imports
from load_story import *

# Defining important variables:
filename = "story.txt"  # To change source file of story, just change this variable name.


# Function to start gameplay:
def start_gameplay():
    # Opening story file and starting gameplay
    game = load_story(filename)
    vertex = game["START"]
    play(game, vertex)


# Function to drive gameplay:
def play(game, vertex):

    # Print the story lines in the current vertex:
    print(vertex)

    # Check if current vertex has other vertices the user can go to.
    # If YES, prompt for input and choose appropriate vertex
    if len(vertex.adjacency_list) != 0:

        # To ensure user inputs something
        valid_input = False
        while not valid_input:
            choice_input = input("\nType a letter choice: ").lower()
            if len(choice_input) == 0:
                print("Empty input! Please type something.")
            else:
                valid_input = True

        # Try getting the next referenced vertex
        try:
            choice_index = ord(choice_input) - 97
            chosen_vertex = vertex.adjacency_list[choice_index]
            next_vertex = game[chosen_vertex]
            play(game, next_vertex)

        # If exception occurs, i.e. the input letter is out of range of available options
        except:
            print("Invalid option. Please try again.")
            play(game, vertex)

    # If NO, then current vertex is the last one. End game.
    else:
        print("\n----------------------------------------------------")
        print("End of story. Please play again!")


# Calling the function to start gameplay:
start_gameplay()
