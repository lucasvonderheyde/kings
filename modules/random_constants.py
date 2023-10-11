from constants import TRY_AGAIN
import random


def random_prompt_until_yes():
    return random.choice(TRY_AGAIN)
    