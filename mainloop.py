from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import input_dialog
import pdb

from modules.get_player_game_info import get_name
from modules.get_player_game_info import get_age
from modules.get_player_game_info import get_difficulty
from classes.Castle import Castle
from classes.King import King
from classes.Human import Human

if __name__ == "__main__":

    easy_castle = Castle("Farming", 500)
    easy_castle_2 = Castle("Forest", 350)
    medium_castle = Castle("Rocky", 500)
    hard_castle = Castle("WINTER DEATH", 700)
    
    first_question_response = yes_no_dialog(
        title= "|_-^KING^-_|",
        text="So you want to be King?").run()
    
    print(first_question_response)

    if first_question_response == True:
        yes_prompt = "What is your name?"
        player_name = get_name(yes_prompt)

    else:
        no_prompt = "Just put your name in."
        player_name = get_name(no_prompt)


    player_age = get_age(player_name)
    player_difficulty = get_difficulty(player_name)
    
    breakpoint()

    if player_difficulty == 0:
        castle = easy_castle or easy_castle_2 
    elif player_difficulty == 1:
        castle = medium_castle
    elif player_difficulty == 2:
        castle = hard_castle


    print("Alright enough from me... go be King ya donk")

    day_counter = 1

    while True:
        print("Day: " + str(day_counter))
        print("A new day in the kingdom...")

        exit_game = input("have you had enough y or n\n")

        if exit_game == "y":
            print("goodbye")
            break

        day_counter += 1
