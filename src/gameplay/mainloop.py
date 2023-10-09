import time

def get_user_name():
    name_input = input("what is your name?")
    print("hmmmmm")
    print("...")
    print("good enough" + name_input + "you're king now.")


if __name__ == "__main__":
    first_question_response = input("So you want to be king?")
    
    if first_question_response.lower() == "yes" or first_question_response.lower() == "y":
        print("Great!")
        get_user_name()
    
    else:
        print("welp to bad someones got to play this 'game'.")
        get_user_name()
