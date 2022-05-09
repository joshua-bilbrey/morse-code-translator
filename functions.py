"""Functions to play dits and dahs and to clear the console."""


import os
from playsound import playsound


def play_dit():
    playsound('./sounds/dit.wav')


def play_dah():
    playsound('./sounds/dah.wav')


def play_silent_dit():
    playsound('./sounds/silent_dit.wav')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
