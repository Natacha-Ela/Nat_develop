import pygame
from global_parameters import Parameters
from menu import menu
from start_run import startRun

pygame.init()

# calling the game
menu()

if Parameters.isRunnung is True:
    startRun()

# when the dino is dead, call menu function to display restart menu
if Parameters.isDead is True:
    menu()


# restart the game
while Parameters.firstTime is False :
    startRun()
    if Parameters.isDead is True:
        menu()
