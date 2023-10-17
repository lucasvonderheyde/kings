from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import button_dialog
import pdb
from modules.get_player_game_info import get_name
from modules.get_player_game_info import get_age
from modules.get_player_game_info import get_difficulty
from classes.Castle import Castle
from classes.King import King
from classes.Human import Human
from classes.Subject import Subject


if __name__ == "__main__":

    #first dialogue
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






    #second dialogue
    player_age = get_age(player_name)
    player_difficulty = get_difficulty(player_name)
    player = King(player_age, player_name, 3, player_difficulty)
    
    
    castle_1 = Castle("Farming", 500)
    castle_2 = Castle("Forest", 350)
    castle_3 = Castle("Rocky", 500)
    castle_4 = Castle("WINTER DEATH", 700)

    print("Alright enough from me... go be King ya donk")

    day_counter = 1

    Subject(25, "Lucas", 4, castle_1, player)
    Subject(18, "Joe", 2, castle_1, player)
    Subject(28, "Lucas", 4, castle_1, player)
    Subject(27, "Nav", 5, castle_1, player)
    Subject(24, "Hanan", 3, castle_1, player)





    #game
    while True:
        button_dialog(
            title= "|_-^KING^-_|",
            text= f"Good Morning, {player.name}",
            buttons= [
                ('Okay', 0)
            ],
        ).run()

        king_castle_pick = button_dialog(
            title= "|_-^KING^-_|",
            text= "Which Castle would you like to go to?",
            buttons= [
                ('castle_1', 0), 
                ('castle_2', 1),
                ('castle_3', 2),
                ('castle_4', 3)
            ],
        ).run()

        def selected_castle(king_castle_pick):
            if king_castle_pick == 0:
                return castle_1            



        print("Day: " + str(day_counter))
        print("A new day in the kingdom...")

        exit_game = input("have you had enough y or n\n")

        if exit_game == "y":
            print("goodbye")
            break

        day_counter += 1
