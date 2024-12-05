#pip install numpy
#pip install windows-curses

import string
import time
import curses
import numpy as np

alphabet = np.array(list(string.ascii_lowercase))

def create_sequence(current_sequence):
    current_sequence = np.append(current_sequence, np.random.choice(alphabet))
    return current_sequence

def display_sequence(stdscr, current_sequence):
    stdscr.clear()
    for letter in current_sequence:
        stdscr.addstr(0, 0, letter)
        stdscr.refresh()
        time.sleep(2)
        stdscr.clear()
        stdscr.refresh()

def get_user_input(stdscr, sequence_length):
    user_input = []
    stdscr.addstr(1, 0, 'Your turn! Press the correct keys!')
    stdscr.refresh()
    time.sleep(3)

    for _ in range(sequence_length):
        key = stdscr.getch()
        user_input.append(chr(key))
        stdscr.refresh()
        time.sleep(0.5)
    return user_input

def check_user_input(current_sequence, user_input):
   if np.array_equal(current_sequence, user_input):
       return True
   else:
       return False

def play_round(stdscr, current_sequence):
    new_sequence = create_sequence(current_sequence)
    display_sequence(stdscr, new_sequence)
    user_input = get_user_input(stdscr, len(new_sequence))

    if check_user_input(new_sequence, user_input):
        stdscr.addstr(2, 0, 'Next level!')
        stdscr.refresh()
        time.sleep(1)
        play_round(stdscr, new_sequence)
    else:
        stdscr.addstr('Sorry, you lose!')
        stdscr.refresh()
        time.sleep(3)

def start_game(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Welcome to Simon Says!')
    stdscr.refresh()
    time.sleep(2)

    current_sequence = np.empty(0, dtype=str)
    play_round(stdscr, current_sequence)


if __name__ == '__main__':
    curses.wrapper(start_game)

