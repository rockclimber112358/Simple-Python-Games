#!/usr/bin/env python2

from Tkinter import *
from ttk import *
from random import *


def gui():
    global word, word_length, clue
    dictionary = ['kernel', 'linux', 'penguin', 'ubuntu', 'python']
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ['_']
    tries = 6

    def hangedman(hangman):
        graphic = ["""
            +-------+
            |
            |
            |
            |
            |
        ==============
        """,
        """
            +-------+
            |       |
            |       O
            |
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |       |
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|
            |
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |      /
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |      / \\
            |
        ===============
        """]
        new_graphic = graphic[hangman]
        hm_graphic.set(new_graphic)
        return

    def game():
        letters_wrong = incorrect_guesses.get()
        letter = guess_letter()
        first_index = word.find(letter)
        if first_index == -1:
            letters_wrong += 1
            incorrect_guesses.set(letters_wrong)
        else:
            for i in range(word_length):
                if letter == word[i]:
                    clue[i] = letter
        hangedman(letters_wrong)
        clue_set = ' '.join(clue)
        word_output.set(clue_set)
        if letters_wrong == tries:
            result_text = 'Game Over.  The word was ' + word + '.'
            result_set.set(result_text)
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)
        elif ''.join(clue) == word:
            result_text = 'You Win! The word was ' + word + '.'
            result_set.set(result_text)
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)

    def guess_letter():
        letter = letter_guess.get()
        letter.strip()
        letter.lower()
        return letter

    def reset_game():
        global word, word_length, clue
        incorrect_guesses.set(0)
        hangedman(0)
        result_set.set('')
        letter_guess.set('')
        word = choice(dictionary)
        word_length = len(word)
        clue = word_length * ['_']
        new_clue = ' '.join(clue)
        word_output.set(new_clue)

    hm_window = Toplevel()
    hm_window.title('Hangman')

    hm_graphic = StringVar()
    word_output = StringVar()
    letter_guess = StringVar()
    incorrect_guesses = IntVar()
    result_set = StringVar()
    player_score = IntVar()
    computer_score = IntVar()

    hangedman(0)
    incorrect_guesses.set(0)
    player_score.set(0)
    computer_score.set(0)

    hm_frame = Frame(hm_window, padding='3 3 12 12', width=300)
    hm_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    hm_frame.columnconfigure(0, weight=1)
    hm_frame.rowconfigure(0, weight=1)

    Label(hm_frame, textvariable=hm_graphic).grid(column=2, row=1)
    Label(hm_frame, textvariable=word_output).grid(column=2, row=2)
    Label(hm_frame, text='Incorrect Guesses:').grid(column=2, row=3)

    Label(hm_frame, text='Enter a letter: ').grid(column=2, row=4)
    hm_entry = Entry(hm_frame, exportselection=0, textvariable=letter_guess).grid(column=2, row=5)
    hm_entry_button = Button(hm_frame, text='Guess', command=game).grid(column=2, row=6)

    Label(hm_frame, text='Wins').grid(column=1, row=7, sticky=W)
    Label(hm_frame, textvariable=player_score).grid(column=1, row=8, sticky=W)
    Label(hm_frame, text='Losses').grid(column=3, row=7, sticky=W)
    Label(hm_frame, textvariable=computer_score).grid(column=3, row=8, sticky=W)
    Label(hm_frame, textvariable=result_set).grid(column=2, row=9)
    replay_button = Button(hm_frame, text='Reset', command=reset_game).grid(column=2, row=10)

if __name__ == '__main__':
    gui()
