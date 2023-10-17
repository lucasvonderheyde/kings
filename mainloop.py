from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import message_dialog
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


def main():

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
     
    castle_1 = Castle("Farming", 0, 500)
    castle_2 = Castle("Forest", 1, 350)
    castle_3 = Castle("Rocky", 2, 500)
    castle_4 = Castle("WINTER DEATH", 3, 700)
    all_castles = Castle.castles

    print("Alright enough from me... go be King ya donk")


    Subject(25, "Lucas", 4, castle_1, player)
    Subject(18, "Joe", 2, castle_1, player)
    Subject(28, "Lucas", 4, castle_1, player)
    Subject(27, "Nav", 5, castle_1, player)
    Subject(24, "Hanan", 3, castle_1, player)
    Subject(78, "manban", 6, castle_2, player)


    day_counter = 1
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
            buttons= which_castle_go_to(player)
        ).run()

        exit_game = input("have you had enough y or n\n")

        if exit_game == "y":
            print("goodbye")
            break

        day_counter += 1

def which_castle_go_to(player):
    buttons = []
    seen_difficulties = set()
    for subject in player.subjects:
        if subject.castle.difficulty not in seen_difficulties:
            buttons.append((subject.castle.biome, subject.castle.difficulty))
            seen_difficulties.add(subject.castle.difficulty)

    return buttons

def selected_castle_info(all_castles, player_difficulty):
    for castle in all_castles:
        if castle.difficutly == player_difficulty:
            castle_info = message_dialog(
                title= f"{castle.biome}",
                text= f"{castle.subjects}").run()
            return castle_info


if __name__ == "__main__":
    main()