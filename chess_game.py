from graphics import *

### constants ###






GRID_LEN = 8

NONE = 0
BLACK = 1
WHITE = 2
FIRST_PLAYER = WHITE

### I CLASS ###

class Game():


    __slots__ = (

        "grid",
        "activePlayer"
    )


    def __init__(self):

        self.grid = [[NONE] * GRID_LEN for i in range(GRID_LEN)]
        self.activePlayer = FIRST_PLAYER


class Piece():


    __slots__= (

        "idontknow"
    )


    def __init__(self):

        self.idontknow= 10



### VI DISPLAY ###

def display_panel():
    ''' Show the panel with 2 different colors for each case

    '''

def display_piece():
    ''' Show a normal piece on the grid undefinetly on their type,while taking in count their color'''
