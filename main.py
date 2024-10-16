#pip install keyboard
#pip install numpy
import string
import time
import keyboard
import numpy as np


alphabet = np.array(list(string.ascii_lowercase))

def create_sequence():
    current_sequence = np.random.choice(alphabet, size=5)
    return current_sequence

def display_sequence(current_sequence):
    print(current_sequence)

def get_user_input():
    time.sleep(5)
    return 'letters'


def check_user_input(current_sequence, user_input):
    if user_input == current_sequence:
        return True
    else:
        return False


def start_game(difficulty=None):
    print('Welcome to Simon Says!')

    current_sequence = create_sequence()
    display_sequence(current_sequence)
    user_input = get_user_input()

    if check_user_input(current_sequence, user_input):
        print('Next level!')
        difficulty +=1
        #ToDo endless loop here
    else:
        print('Sorry, you lose!')

    print('Press esc to exit')
    keyboard.wait('esc')

if __name__ == '__main__':
    start_game()

