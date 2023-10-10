import sys
from prompt_toolkit.shortcuts import yes_no_dialog

from modules.get_name_age_difficulty import get_name_age_difficulty
from castle import Castle
from classes.king import King

sys.path.insert(0, "kings/src/classes")

if __name__ == "__main__":

    easy_castle = Castle("Farming", 500)
    easy_castle_2 = Castle("Forest", 350)
    medium_castle = Castle("Rocky", 500)
    hard_castle = Castle("WINTER DEATH", 700)

    

    first_question_response = yes_no_dialog(
        title= "|_-^KING^-_|",
        text="So you want to be King?".run()
    )
    
    print(first_question_response)

    breakpoint

    # input("So you want to be king?\n")
    
    if first_question_response.lower() == "yes" or first_question_response.lower() == "y":
        print("Great!")
    
    else:
        print("welp to bad someones got to play this 'game'.")

    name, age, difficulty = get_name_age_difficulty() 

    # def select_difficulty(difficulty):

    #     if difficulty.lower() == "easy":
            
    #     elif difficulty.lower() == "medium":

    #     elif difficulty.lower() == "hard":

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