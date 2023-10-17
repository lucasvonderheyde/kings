from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import button_dialog
from modules.random_constants import random_prompt_until_yes


def get_name(prompt):
    
    name = input_dialog(
            title= "|_-^KING^-_|",
            text= prompt).run()
        
    while name == None:
        random_prompt = random_prompt_until_yes()

        name = input_dialog(
            title= "|_-^KING^-_|",
            text= random_prompt).run()
        
    return name
        
def get_age(name):

    age = input_dialog(
            title= "|_-^KING^-_|",
            text= f"Alright {name} what's your age?").run()
        
    while age == None:

        age = input_dialog(
            title= "|_-^KING^-_|",
            text= "We've been through this already, just put in your age donk.").run()
        
    return age


def get_difficulty(name):

    difficulty = button_dialog(
        title= "|_-^KING^-_|",
        text= f"Time to choose the difficulty {name}",
        buttons= [
            ('Easy', 0),
            ('Medium', 1),
            ('Death', 2)
        ],
    ).run()

    return difficulty
