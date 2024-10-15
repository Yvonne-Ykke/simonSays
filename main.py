#pip install keyboard
import keyboard

#def create_sequence():

#def display_sequence():


#def get_user_input():


def check_user_input(sequence, user_input):
    if user_input == sequence:
        return True


def start_game():
    print('Welcome to Simon Says!')
    keyboard.wait('esc')

if __name__ == '__main__':
    start_game()

