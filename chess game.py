############ DISCLAMER ############

# In this whole program :
#
# LEN        --> Length
# SQU        --> Case
# ABS        --> Abscissa
# ORD        --> Ordinate

# SQU_ABS    --> Abscissa of square
# SQU_ORD    --> Ordinate of square



from graphics import *


### constants ###




#info de grille
LEN_PANEL = 200
LEN_GRID = 600
NBR_SQU = 8
LEN_CASE = LEN_GRID // NBR_SQU
LEN_MID_CASE = LEN_CASE // 2
PANEL_COLOR1 = couleur(130,35,1) #brown
PANEL_COLOR2 = couleur(225,224,163) #beige
CONFIG_COLOR3 = couleur(37,39,114) #blue

RAY_PIECE = 25

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

        self.grid = [[NONE] * NBR_SQU for nbr_square in range(NBR_SQU)]
        self.activePlayer = FIRST_PLAYER


class Piece():


    __slots__= (

        "color"
        "type"
    )


    def __init__(self):

        self.color = WHITE
        self.type = PAWN



### II INITIALIZATION ###

def init_game ():
    G = Game()

    return G
    """game loaded with panel and piece (version 1, same piece then chess piece) """

def end_game(G):
    """ end of the game if Mate"""

### III UTILITIES ###

def get_abs(click):
    """return abs in grid"""

    CLICK_ABS = click.x//LEN_CASE

    return CLICK_ABS

def get_ord(click):
    """return ord in grid"""

    CLICK_ORD = click.y//LEN_CASE
    return CLICK_ORD


def ennemy():
    """optional: can't play if not your turn"""


### IV DROP PIECES ###

def drop_piece():
    """ drop a piece"""

    G.grid[ABS][ORD]=G.activePlayer

def select_piece():
    """select the piece you click on"""

def delete_piece():
    """erase the piece that move"""

def valid_move():
    """see later if one or more"""

def valid_case():
    """if u can drop a piece on """

### VI DISPLAY ###

def display_panel():
    ''' Show the panel with 2 different colors for each case'''

    for SQU_ABS in range(0,NBR_SQU):

        for SQU_ORD in range(0,NBR_SQU):

            if SQU_ABS%2 == 0 and SQU_ORD%2 == 0 or SQU_ABS%2 != 0 and SQU_ORD%2 != 0:
            # If square abs and ord are even or if square abs and ord are odd

                affiche_rectangle_plein(Point(LEN_CASE*SQU_ABS,LEN_CASE*SQU_ORD),Point(LEN_CASE*(SQU_ABS+1),LEN_CASE*(SQU_ORD+1)),PANEL_COLOR1)

            else :
                affiche_rectangle_plein(Point(LEN_CASE*SQU_ABS,LEN_CASE*SQU_ORD),Point(LEN_CASE*(SQU_ABS+1),LEN_CASE*(SQU_ORD+1)),PANEL_COLOR2)




def display_piece():
    ''' Show a normal piece on the grid regardless of their type, while taking in count their color'''

    for ABS in range (0,NBR_SQU):
        for ORD in range (0,NBR_SQU):
            if G.grid[ABS][ORD]==BLACK:
                affiche_cercle_plein(Point(ABS*LEN_CASE+LEN_CASE//2,ORD*LEN_CASE+LEN_CASE//2),RAY_PIECE, noir)
            elif G.grid[ABS][ORD]==WHITE:
                affiche_cercle_plein(Point(ABS*LEN_CASE+LEN_CASE//2,ORD*LEN_CASE+LEN_CASE//2),RAY_PIECE, blanc)


def display_config_panel(G):
    ''' for mater, change color, timer, numer of piece..'''
    affiche_rectangle_plein(Point(LEN_GRID,0),Point(LEN_GRID+LEN_PANEL,LEN_GRID),CONFIG_COLOR3)
def display_piece_selection():
    '''show which piece is selected'''





def display_game(J):
    """
    Affiche toutes les composantes du jeu
    """
    display_panel()
    display_config_panel(G)
    display_piece()
    affiche_tout()


### VII MAIN ###

init_fenetre(LEN_GRID+LEN_PANEL,LEN_GRID,"Chess Game")
affiche_auto_off()

G = init_game()
display_game(G)
click = Point()


while not(end_game(G)) and pas_echap():

    click = wait_clic()

    if click.x < LEN_GRID: # we r on the panel

        CLICK_ABS = get_abs(click)
        CLICK_ORD = get_ord(click)
        if G.grid[CLICK_ABS][CLICK_ORD] != NONE:
            select_piece(G,CLICK_ABS,CLICK_ORD) # select the piece
            G.activePlayer == G.grid[CLICK_ABS][CLICK_ORD] # color of player become the one of the selected piece

        elif G.grid[CLICK_ABS][CLICK_ORD] == NONE: #no piece
            """ and select_piece(G)"""  # and a piece selected before
            drop_piece(G,CLICK_ABS,CLICK_ORD)    # drop a piece on the case selcted (2nd clic)
            """delete_piece (G,CLICK_ABS,CLICK_ORD)""" # take off the piece (1st piece)
    # nothing if not on panel
    display_game(G)
attendre_echap()
