############ DISCLAMER ############

# In this whole program :
#
# LEN        --> Length
# SQU        --> Case
# PIX_ABS        --> Abscissa
# PIX_ORD        --> Ordinate

# ABS    --> Abscissa of square
# ORD    --> Ordinate of square


from graphics import *


### constants ###




#info de grille
LEN_PANEL = 200
LEN_GRID = 600
NBR_SQU = 8
LEN_CASE = LEN_GRID // NBR_SQU
LEN_MID_CASE = LEN_CASE // 2
PANEL_COLOR1 = couleur(130,35,1)        #brown
PANEL_COLOR2 = couleur(225,224,163)     #beige
CONFIG_COLOR3 = couleur(37,39,114)      #blue
ACTIVE_SQU = couleur(125,125,125)       #grey

RAY_PIECE = 25

NONE =  0
WHITE = 1
BLACK = 2

PAWN = 3
KNIGHT = 4
BISHOP = 5
ROOK = 6
QUEEN = 7
KING = 8

PIECE_LIST = (PAWN,KNIGHT,BISHOP,ROOK,QUEEN,KING)   #List of all possible pieces

ROOK_DIR=[[1,0],[0,1],[0,-1],[-1,0]]                #List of rook possible moves

FIRST_PLAYER = WHITE

### I CLASS ###

class Game():

    """

    Contains all chess information :

        grid : Game Grid, list of ABS and ORD : Tells us on which location are pieces
        activePlayer : In-game active player. Stores BLACK or WHITE
        selectedSquare : after 1 click on a piece, store location of selected piece
        validSquares : Stores all the valid squares after a piece has been selected
        arrivalSquare : after a piece has been selected and a new click, store arrival piece location.
        piece : initialize class piece

    """
    __slots__ = (

        "grid",
        "activePlayer",
        "selectedSquare",
        "validSquares",
        "arrivalSquare",
        "piece"
    )


    def __init__(self):

        """
        grid : List of all possible squares in-game
        selectedSqaure and arrivalSqaure : Tuple, easy to clear and fill because only 1 entry at a time

        """
        self.grid = [[NONE] * NBR_SQU for nbr_square in range(NBR_SQU)]
        self.activePlayer = FIRST_PLAYER
        self.selectedSquare = None
        self.validSquares = []
        self.arrivalSquare = ()
        self.piece = Piece()




class Piece():
    """
    Contains all chess piece information :
        color : list of possible colors
        type : list of all possible types

    """

    __slots__= (

        "color",
        "type"
    )


    def __init__(self):

        self.color = [WHITE, BLACK]
        self.type = PIECE_LIST




### II INITIALIZATION ###

def init_game ():
    """game loaded with panel and piece"""
    G = Game()

    for column in range (NBR_SQU):

        G.grid[column][1]=PAWN_W
        G.grid[column][6]=PAWN_B

    for column in range (0,8,7):

        G.grid[column][0]=ROOK_W
        G.grid[column][7]=ROOK_B

    for column in range (1,8,5):

        G.grid[column][0]=KNIGHT_W
        G.grid[column][7]=KNIGHT_B

    for column in range (2,8,3):

        G.grid[column][0]=BISHOP_W
        G.grid[column][7]=BISHOP_B

    G.grid[4][0]=QUEEN_W
    G.grid[4][7]=QUEEN_B

    G.grid[3][0]=KING_W
    G.grid[3][7]=KING_B


    G.grid[3][4]=ROOK_W
    return G


def init_piece():
    """ Initialize class Piece """
    P = Piece()


    return P

def end_game(G):
    """ end of the game if Mate"""
    pass
### III UTILITIES ###

def get_abs(clic):
    """return square abs in grid"""

    CLICK_ABS = clic.x//LEN_CASE

    return CLICK_ABS

def get_ord(clic):
    """return square ord in grid"""

    CLICK_ORD = clic.y//LEN_CASE
    return CLICK_ORD


def what_is_selected_piece(G):
    """return piece type and color"""
    Piece=G.grid[G.selectedSquare[0]][G.selectedSquare[1]]
    return Piece


def piece_color(COLOR):
    """change color in CAPITAL letters (initialized like this) in color in lowercase letters (for display color)"""
    color=None
    if COLOR == WHITE:
        color=blanc
    elif COLOR == BLACK:
        color=noir
    return color


def piece_display_type(TYPE):
    """ check what piece it is and return display_'Piece name' """
    display_type=None
    if TYPE == PAWN:
        display_type = display_pawn
    elif TYPE == ROOK:
        display_type = display_rook
    elif TYPE == BISHOP:
        display_type = display_bishop
    elif TYPE == KNIGHT:
        display_type = display_knight
    elif TYPE == QUEEN:
        display_type = display_queen
    else:
        display_type = display_king
    return display_type

def piece_move_type(TYPE):
    """ check what piece it is and return move_'Piece name' """
    move_type=None
    if TYPE == PAWN:
        move_type = move_pawn
    elif TYPE == ROOK:
        move_type = move_rook
    elif TYPE == BISHOP:
        move_type = move_bishop
    elif TYPE == KNIGHT:
        move_type = move_knight
    elif TYPE == QUEEN:
        move_type = move_queen
    else:
        move_type = move_king
    return move_type



def store_arrivalSquare(G,ABS,ORD):

    G.arrivalSquare=(ABS,ORD)

def are_color_different(G,ABS,ORD):
    """return whether selectedPiece's color and entryPiece's color are different"""
    if G.grid[ABS][ORD] != NONE and what_is_selected_piece(G)[0] == G.grid[ABS][ORD][0]:
        return True


### IV DROP PIECES ###

def drop_piece(G):
    """ drop a piece"""

    Piece = what_is_selected_piece(G)
    G.grid[G.arrivalSquare[0]][G.arrivalSquare[1]]=Piece
    delete_piece (G)  # take off the piece (1st piece)

def select_piece(G,ABS,ORD):
   """select the piece you click on"""

   G.selectedSquare = (ABS,ORD)
   valid_square(G,ABS,ORD)


def valid_square(G,ABS,ORD):
    G.validSquares=[]
    PIECE=G.selectedSquare
    piece_movetype = piece_move_type(G.grid[PIECE[0]][PIECE[1]][1])
    piece_movetype(G)


def position_vide(G,ABS,ORD):
    condition=False
    if G.grid[ABS][ORD]==NONE:
        condition=True
    return condition



def is_in_valid_square(G):
    """"Check if selected square is in validSquare"""
    condition=False
    for value in G.validSquares:

        if value == G.arrivalSquare:
            condition=True
        value=+1
    return condition


def move_rook(G):

   for x in range(NBR_SQU):
        for y in range(NBR_SQU):
            if position_vide(G,x,y):
                G.validSquares.append((x,y))





def is_in_grid(posx,posy):
    """ Check if square is still in the game grid"""
    return 0<=posx<NBR_SQU and 0<=posy<NBR_SQU


def delete_piece(G):
    """deletes piece after moving"""
    G.grid[G.selectedSquare[0]][G.selectedSquare[1]] = NONE

    G.selectedSquare = ()



def valid_move(P,G,direction,player,ABS,ORD):
    """check is move is valid"""
    if G.selectedSquare != NONE:

        PIECE=G.grid[G.selectedSquare[0]][G.selectedSquare[1]]

        move_type = piece_move_type(PIECE[1])

        move_type(G,direction,player,ABS,ORD)


### VI DISPLAY ###

def display_panel():
    """ Show the panel with 2 different colors for each case"""

    for ABS in range(0,NBR_SQU):

        for ORD in range(0,NBR_SQU):

            if ABS%2 == 0 and ORD%2 == 0 or ABS%2 != 0 and ORD%2 != 0:
            # If square abs and ord are even or if square abs and ord are odd

                affiche_rectangle_plein(Point(LEN_CASE*ABS,LEN_CASE*ORD),Point(LEN_CASE*(ABS+1),LEN_CASE*(ORD+1)),PANEL_COLOR1)

            else :
                affiche_rectangle_plein(Point(LEN_CASE*ABS,LEN_CASE*ORD),Point(LEN_CASE*(ABS+1),LEN_CASE*(ORD+1)),PANEL_COLOR2)



def display_piece(G,P):
    """ Display all game pieces, including their color and type """

    for ABS in range (0,NBR_SQU):
        for ORD in range (0,NBR_SQU):

            if G.grid[ABS][ORD] != NONE:

                PIECE=G.grid[ABS][ORD]

                color = piece_color(PIECE[0])

                display_type = piece_display_type(PIECE[1])
                display_type(ABS,ORD,color)



def display_pawn(ABS,ORD,color):
    """ Displays pawn """
    RAYON=LEN_CASE//6

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2+RAYON),RAYON-RAYON//3,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2),RAYON,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2-RAYON),RAYON+RAYON//3,color)

def display_rook(ABS,ORD,color):
    """ Displays rook """
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +2*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +2*LEN_CASE//10),Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +7*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//9, ORD*LEN_CASE +7*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +2*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +4*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +5*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +6*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +7*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)

def display_bishop(ABS,ORD,color):
    """ Displays bishop """
    RAYON=LEN_CASE//4

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2+RAYON),RAYON//3,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2),RAYON,color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),color)

def display_king(ABS,ORD,color):
    """ Displays king """
    RAYON=LEN_CASE//15

    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +4*LEN_CASE//10),Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),Point(ABS*LEN_CASE +2*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +4*LEN_CASE//10),Point(ABS*LEN_CASE +5*LEN_CASE//10, ORD*LEN_CASE +5*LEN_CASE//10),Point(ABS*LEN_CASE +4*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +4*LEN_CASE//10),Point(ABS*LEN_CASE +5*LEN_CASE//10, ORD*LEN_CASE +5*LEN_CASE//10),Point(ABS*LEN_CASE +6*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +4*LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),Point(ABS*LEN_CASE +5*LEN_CASE//10, ORD*LEN_CASE +5*LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +2*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),RAYON,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +4*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),RAYON,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +6*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),RAYON,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +8*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),RAYON,color)


def display_queen(ABS,ORD,color):
    """ Displays queen """
    RAYON=LEN_CASE//4

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//3, ORD*LEN_CASE +LEN_CASE//2),RAYON,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +2*LEN_CASE//3, ORD*LEN_CASE +LEN_CASE//2),RAYON,color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//5, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +4*LEN_CASE//5, ORD*LEN_CASE +2*LEN_CASE//5),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//7, ORD*LEN_CASE +LEN_CASE//2),Point(ABS*LEN_CASE +4*LEN_CASE//7, ORD*LEN_CASE +17*LEN_CASE//20),color)


def display_knight(ABS,ORD,color):
    """ Displays knight """
    if color == blanc:
        other=noir
    else:
        other=blanc

    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//2),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//2),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +7*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +9*LEN_CASE//20),Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//2),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//2),Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +9*LEN_CASE//20),Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +6*LEN_CASE//10, ORD*LEN_CASE +7*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//10, ORD*LEN_CASE + 7*LEN_CASE//10),Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +6*LEN_CASE//10),LEN_CASE//25,other)


def display_config_panel(G):
    """ for meter, change color, timer, numer of piece.."""
    affiche_rectangle_plein(Point(LEN_GRID,0),Point(LEN_GRID+LEN_PANEL,LEN_GRID),CONFIG_COLOR3)


def display_piece_selection(G):
    """Draw a box around selectedSquare"""

    if G.selectedSquare:
        affiche_rectangle(Point(G.selectedSquare[0]*LEN_CASE,G.selectedSquare[1]*LEN_CASE),Point((G.selectedSquare[0]+1)*LEN_CASE,(G.selectedSquare[1]+1)*LEN_CASE),rouge,5)


def display_valid_squ(G):
    """Draw a box around validSquares"""
    if G.selectedSquare:
        for i in range(len(G.validSquares)):

            ABS=G.validSquares[i][0]
            ORD=G.validSquares[i][1]
            affiche_rectangle_plein(Point(ABS*LEN_CASE,ORD*LEN_CASE), Point((ABS+1)*LEN_CASE,(1+ORD)*LEN_CASE),ACTIVE_SQU)


def display_game(G):
    """ Dispalys all game components"""
    display_panel()
    display_config_panel(G)
    display_valid_squ(G)
    display_piece(G,P)
    display_piece_selection(G)
    affiche_tout()


### VII MAIN ###

init_fenetre(LEN_GRID+LEN_PANEL,LEN_GRID,"Chess Game")
affiche_auto_off()



P = init_piece()

PAWN_W = (P.color[0], P.type[0])
PAWN_B = (P.color[1], P.type[0])

KNIGHT_W = (P.color[0], P.type[1])
KNIGHT_B = (P.color[1], P.type[1])

BISHOP_W = (P.color[0], P.type[2])
BISHOP_B = (P.color[1], P.type[2])

ROOK_W = (P.color[0], P.type[3])
ROOK_B = (P.color[1], P.type[3])

QUEEN_W = (P.color[0], P.type[4])
QUEEN_B = (P.color[1], P.type[4])

KING_W = (P.color[0], P.type[5])
KING_B = (P.color[1], P.type[5])


G = init_game()
display_game(G)



while not(end_game(G)) and pas_echap():

    clic = wait_clic()
    if clic.x < LEN_GRID: # we are on the panel
        ABS = get_abs(clic)
        ORD = get_ord(clic)

        if G.grid[ABS][ORD] != NONE and not(G.selectedSquare):
            select_piece(G,ABS,ORD) # select the piece



        elif G.selectedSquare: #no piece and a piece selected before
            store_arrivalSquare(G,ABS,ORD)
            if is_in_valid_square(G):

                drop_piece(G)    # drop a piece on the case selcted (2nd clic)

            else:
                G.selectedSquare=()


    # nothing if not on panel

    display_game(G)
attendre_echap()
