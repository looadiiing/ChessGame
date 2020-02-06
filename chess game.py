from graphics import *


### constants ###




#info de grille
LEN_PANEL = 200
LEN_GRID = 600
NBR_CASE = 8
LEN_CASE = LEN_GRID // NBR_CASE
PANEL_COLOR1 = couleur(130,35,1) #brown
PANEL_COLOR2 = couleur(225,224,163) #beige

RAY_PIECE= 25

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

        self.grid = [[NONE] * LEN_GRID for i in range(GRID_LEN)]
        self.activePlayer = FIRST_PLAYER


class Piece():


    __slots__= (

        "color"
        "type"
    )


    def __init__(self):

        self.color = WHITE
        self.type = PIECE



### II INITIALISATION ###

def init_game ():
    """game loaded with panel and piece (1 version, same piece then chess piece) """

def end_game(G):
    """ end of the game if checkmat"""

### III UTILITIES ###

def get_abs():
    """return abs in grid"""


def get_ord():
    """return ord in grid"""

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
    ''' Show the panel with 2 different colors for each case

    '''

def display_piece():
    ''' Show a normal piece on the grid undefinetly on their type,while taking in count their color'''
    for i in range (0,LEN_GRID):
        for j in range (0,LEN_GRID):
            if G.grid[ABS][ORD]==BLACK:
                affiche_cercle_plein(Point(ABS*LEN_CASE+LEN_CASE//2,ORD*LEN_CASE+LEN_CASE//2),RAY_PIECE, noir)
            elif G.grid[ABS][ORD]==WHITE:
                affiche_cercle_plein(Point(ABS*LEN_CASE+LEN_CASE//2,ORD*LEN_CASE+LEN_CASE//2),RAY_PIECE, blanc)
                
                
def display_config_panel ():
    ''' for mater, change color, timer, numer of piece..'''


def display_piece_selection():
    '''show which piece is selected'''





def display_game(J):
    """
    Affiche toutes les composantes du jeu
    """
    display_panel()
    display_config_panel()
    display_piece()
    affiche_tout()


### VII MAIN ###

init_fenetre(LEN_GRID+LEN_PANEL,LEN_GRID,"Chess Game")
affiche_auto_off()

G = init_game()
display_game(G)
clic = Point()


while not(end_game(G)) and pas_echap():
    clic = wait_clic()
    if clic.x < LEN_GRID: # we r on the panel
        ABS1 = get_abs(clic)
        ORD1 = get_ord(clic)
        if G.grid[ABS1][ORD1] != NONE:
            select_piece(G,ABS1,ORD1) # select the piece
            G.activePlayer == G.grid[ABS1][ORD1] # color of player become the one of the selected piece
            clic = wait_clic()
            if clic.x < LEN_GRID: # we r on the panel
                ABS2 = get_abs(clic)
                ORD2 = get_ord(clic)
                if G.grid[ABS2][ORD2] == NONE: # no piece on the grid
                    drop_piece(G,ABS2,ORD2)    # drop a piece on the case selcted (2nd clic)
                    delete_piece (G,ABS1,ORD1) # take off the piece (1st piece)
    # nothing if not on panel
    display_game(G)
attendre_echap()
