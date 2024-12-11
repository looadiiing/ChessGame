############ DISCLAMER ############

# In this whole program :
#
# LEN       --> Length
# SQU       --> Case
# PIX_ABS   --> Abscissa
# PIX_ORD   --> Ordinate

# ABS       --> Abscissa of square
# ORD       --> Ordinate of square


from graphics import *




### 0 CONSTANTS ###

# Game Lengths sizes

NBR_SQU = 8
LEN_PANEL = 200
LEN_GRID = 600
LEN_GAME = LEN_PANEL + LEN_GRID
LEN_CASE = LEN_GRID // NBR_SQU


# Game Colors

PANEL_COLOR1 = couleur(130,35,1)        # brown
PANEL_COLOR2 = couleur(225,224,163)     # beige
CONFIG_COLOR3 = couleur(37,39,114)      # blue
ACTIVE_SQU_COLOR = couleur(125,125,125) # grey


# Game Constants

NONE = 0
WHITE = 1
BLACK = 2

PAWN = 3
ROOK = 4
KNIGHT = 5
BISHOP = 6
QUEEN = 7
KING = 8

PAWN_DIR = ((-1,1),(0,1),(0,2),(1,1))                                   # List of all pawn vectorial possible moves
ROOK_DIR = ((-1,0),(0,1),(1,0),(0,-1))                                  # List of all rook vectorial possible moves
KNIGHT_DIR = ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2))  # List of all knight vectorial possible moves
BISHOP_DIR = ((-1,-1),(-1,1),(1,1),(1,-1))                              # List of all bishop vectorial possible moves
QUEEN_DIR = BISHOP_DIR + ROOK_DIR                                       # List of all queen vectorial possible moves (Bishop + rook ones)
KING_DIR = QUEEN_DIR                                                    # List of all king vectorial possible moves (Same as queen)

COLOR_LIST = (WHITE, BLACK)                                                     # List of all colors
PIECE_LIST = (PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING)                          # List of all pieces
DIR_LIST = (PAWN_DIR, ROOK_DIR, KNIGHT_DIR, BISHOP_DIR, QUEEN_DIR, KING_DIR)    # List of all directions for each piece

FIRST_PLAYER = WHITE    # First payer to play

### I CLASS ###

class Game():


    """
    Contains all chess information :

        grid            : Game Grid, list of ABS and ORD : Tells us on which location are pieces
        activePlayer    : In-game active player. Stores BLACK or WHITE
        selectedSquare  : After 1 click on a piece, store location of selected piece
        validSquares    : Stores all the valid squares after a piece has been selected
        arrivalSquare   : After a piece has been selected : a new click store arrival piece location.
        piece           : Initializes class piece

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
        grid                            : List of all possible squares in-game
        selectedSquare / arrivalSquare  : Tuple, easy to clear and fill because only 1 entry at a time
        validSquares                    : List, need to fill new squares and delete them
        """

        self.grid = [[NONE] * NBR_SQU for nbr_square in range(NBR_SQU)]
        self.activePlayer = FIRST_PLAYER
        self.selectedSquare = ()
        self.validSquares = []
        self.arrivalSquare = ()
        self.piece = Piece()


class Piece():


    """
    Contains all chess piece information :

        color   : list of possible colors
        type    : list of all possible types

    """
    __slots__ = (

        "color",
        "type"
    )

    def __init__(self):

        self.color = COLOR_LIST
        self.type = PIECE_LIST



### II INITIALIZATION ###

def init_game ():
    """Game loaded with class game + all pieces"""

    # Initialize class game
    G = Game()

    # Places all games pieces on the grid :
    # loops to create pieces on both sides

    for column in range (NBR_SQU):
        G.grid[column][1] = PAWN_W
        G.grid[column][6] = PAWN_B

    for column in range (0,8,7):
        G.grid[column][0] = ROOK_W
        G.grid[column][7] = ROOK_B

    for column in range (1,8,5):
        G.grid[column][0] = KNIGHT_W
        G.grid[column][7] = KNIGHT_B

    for column in range (2,8,3):
        G.grid[column][0] = BISHOP_W
        G.grid[column][7] = BISHOP_B

    G.grid[4][0] = QUEEN_W
    G.grid[4][7] = QUEEN_B

    G.grid[3][0] = KING_W
    G.grid[3][7] = KING_B


    #!!!! TEST !!!!#

    G.grid[3][4] = KING_W

    #!!!! TEST !!!!#
    return G


def init_piece():
    """Initialize class Piece"""

    P = Piece()

    return P


def end_game(G):
    """End of the game if Mate"""

    pass




### III UTILITIES ###

def get_abs(clic):
    """Return square abs in grid"""

    CLICK_ABS = clic.x // LEN_CASE

    return CLICK_ABS

def get_ord(clic):
    """Return square ord in grid"""

    CLICK_ORD = clic.y // LEN_CASE

    return CLICK_ORD


def what_is_selected_piece(G):
    """Return piece type and color"""

    Piece = G.grid[G.selectedSquare[0]][G.selectedSquare[1]]

    return Piece


def piece_color(COLOR):
    """Change color in CAPITAL letters (initialized like this) in color in lowercase letters (for display color)"""

    color = None

    if COLOR == WHITE:
        color = blanc
    else:
        color = noir

    return color


def piece_display_type(TYPE):
    """Check what piece it is and return display_'Piece name'"""

    display_type = None

    if TYPE == PAWN:
        display_type = display_pawn
    elif TYPE == ROOK:
        display_type = display_rook
    elif TYPE == KNIGHT:
        display_type = display_knight
    elif TYPE == BISHOP:
        display_type = display_bishop
    elif TYPE == QUEEN:
        display_type = display_queen
    else:
        display_type = display_king

    return display_type


def piece_move_type(TYPE):
    """Check what piece it is and return move_'Piece name'"""

    move_type = None

    if TYPE == PAWN:
        move_type = move_pawn
    elif TYPE == ROOK:
        move_type = move_rook
    elif TYPE == KNIGHT:
        move_type = move_knight
    elif TYPE == BISHOP:
        move_type = move_bishop
    elif TYPE == QUEEN:
        move_type = move_queen
    else:
        move_type = move_king

    return move_type


def is_in_grid(ABS,ORD):
    """Returns True if square is still in the game grid"""

    condition = False
    if 0<=ABS<NBR_SQU and 0<=ORD<NBR_SQU:
        condition = True
    return condition


def are_same_color(G,ABS,ORD):
    """Returns True if selectedPiece's color and entryPiece's color are the same"""

    condition = False

    if what_is_selected_piece(G)[0] == G.grid[ABS][ORD][0]:
        condition = True
    return condition


def empty_pos(G,ABS,ORD):
    """Returns True if the pos is empty"""

    condition = False

    if G.grid[ABS][ORD] == NONE:
        condition = True

    return condition




### IV DROP PIECES ###

def select_piece(G,ABS,ORD):
    """Stores the piece you click on in G.selectedSquare and display all squares this Piece can go to"""

    G.selectedSquare = (ABS,ORD)

    valid_square(G,ABS,ORD)


def store_arrivalSquare(G,ABS,ORD):
    """After 2nd click, stores square in G.arrivalSquare"""

    G.arrivalSquare = (ABS,ORD)


def drop_piece(G):
    """Drops the selectedSquare Piece on arrivalSquare then deletes it from selectedSquare"""

    PIECE = what_is_selected_piece(G)
    G.grid[G.arrivalSquare[0]][G.arrivalSquare[1]] = PIECE

    delete_piece (G)  # take off the piece (1st piece)


def delete_piece(G):
    """Deletes piece after moving"""

    G.grid[G.selectedSquare[0]][G.selectedSquare[1]] = NONE

    G.selectedSquare = ()


def is_in_valid_square(G):
    """"Check if arrivalSquare is in the validSquare list"""

    condition = False

    for square in G.validSquares:
        if square == G.arrivalSquare:
            condition = True

    return condition


def valid_square(G,ABS,ORD):
    """Empty the G.validSquares list and reupdates it with the current selectedPiece"""

    G.validSquares = []

    # Stores the piece's name in piece_movetype. If a PAWN is on [ABS][ORD] :
    # piece_move_type(G.grid[ABS][ORD][1]) will return the text 'move_pawn'
    PIECE = G.grid[G.selectedSquare[0]][G.selectedSquare[1]] # Stores selectedPieces color/type
    piece_movetype = piece_move_type(PIECE[1])

    # function called here is actually named 'piece_"pieceName"'
    piece_movetype(G)


def move_pawn(G):
    """Stores all the pawn validSquares"""

    pass


def move_rook(G):
    """Stores all the rook validSquares"""

    DIR_LIST = ROOK_DIR
    ABS = G.selectedSquare[0]
    ORD = G.selectedSquare[1]
    LOOP=True

    for LIST_NBR in DIR_LIST:
        move_dir(G,ABS,ORD,LIST_NBR,LOOP)



def move_knight(G):
    """Stores all the knight validSquares"""

    pass


def move_bishop(G):
    """Stores all the rook validSquares"""

    DIR_LIST = BISHOP_DIR
    ABS = G.selectedSquare[0]
    ORD = G.selectedSquare[1]
    LOOP=True

    for LIST_NBR in DIR_LIST:
        move_dir(G,ABS,ORD,LIST_NBR,LOOP)


def move_queen(G):
    """Stores all the rook validSquares"""

    pass


def move_king(G):
    """Stores all the rook validSquares"""

    DIR_LIST = KING_DIR
    ABS = G.selectedSquare[0]
    ORD = G.selectedSquare[1]
    LOOP=False

    for LIST_NBR in DIR_LIST:
        move_dir(G,ABS,ORD,LIST_NBR,LOOP)


def move_dir(G,ABS,ORD,LIST_NBR,LOOP):
    """Stores valid positions for one direction"""

    ABS += LIST_NBR[0]
    ORD += LIST_NBR[1]

    Condition=True

    while is_in_grid(ABS,ORD) and Condition==True:

        if G.grid[ABS][ORD] == NONE:
            G.validSquares.append((ABS,ORD))

        else:
            if not are_same_color(G,ABS,ORD):
                G.validSquares.append((ABS,ORD))
                return G

            if are_same_color(G,ABS,ORD):
                return G

        if LOOP== True:
            ABS += LIST_NBR[0]
            ORD += LIST_NBR[1]
        else:
            Condition=False


def squ_valid(G,ABS,ORD,LIST_NBR):

    ABS += LIST_NBR[0]
    ORD += LIST_NBR[1]

    if G.grid[ABS][ORD] == NONE:
            G.validSquares.append((ABS,ORD))

    else:
        if not are_same_color(G,ABS,ORD):
            G.validSquares.append((ABS,ORD))
            return G

        if are_same_color(G,ABS,ORD):
            return G




### VI DISPLAY ###

def display_panel():
    """Show the panel with 2 different colors for each case"""

    for ABS in range(0,NBR_SQU):
        for ORD in range(0,NBR_SQU):
            if ABS%2 == 0 and ORD%2 == 0 or ABS%2 != 0 and ORD%2 != 0:
            # If square abs and ord are even or if square abs and ord are odd
                affiche_rectangle_plein(Point(LEN_CASE*ABS,LEN_CASE*ORD),Point(LEN_CASE*(ABS+1),LEN_CASE*(ORD+1)),PANEL_COLOR1)

            else :
                affiche_rectangle_plein(Point(LEN_CASE*ABS,LEN_CASE*ORD),Point(LEN_CASE*(ABS+1),LEN_CASE*(ORD+1)),PANEL_COLOR2)



def display_piece(G,P):
    """Display all game pieces, including their color and type"""

    for ABS in range (0,NBR_SQU):
        for ORD in range (0,NBR_SQU):
            if G.grid[ABS][ORD] != NONE:
                PIECE = G.grid[ABS][ORD]
                color = piece_color(PIECE[0])

                # Stores the piece's name in piece_movetype. If a PAWN is on [ABS][ORD] :
                # piece_display_type(G.grid[ABS][ORD][0]) will return the text 'display_pawn'

                display_type = piece_display_type(PIECE[1])

                # function called here is actually named 'piece_"pieceName"'
                display_type(ABS,ORD,color)


def display_pawn(ABS,ORD,color):
    """Displays pawn"""

    RADIUS = LEN_CASE//6

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2+RADIUS),RADIUS-RADIUS//3,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2),RADIUS,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2-RADIUS),RADIUS+RADIUS//3,color)

def display_rook(ABS,ORD,color):
    """Displays rook"""

    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +2*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +2*LEN_CASE//10),Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +7*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//9, ORD*LEN_CASE +7*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +2*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +4*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +5*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +6*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +7*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)

def display_bishop(ABS,ORD,color):
    """Displays bishop"""

    RADIUS = LEN_CASE//4

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2+RADIUS),RADIUS//3,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2),RADIUS,color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),color)

def display_king(ABS,ORD,color):
    """Displays king"""

    RADIUS = LEN_CASE//15

    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +4*LEN_CASE//10),Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),Point(ABS*LEN_CASE +2*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +4*LEN_CASE//10),Point(ABS*LEN_CASE +5*LEN_CASE//10, ORD*LEN_CASE +5*LEN_CASE//10),Point(ABS*LEN_CASE +4*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +4*LEN_CASE//10),Point(ABS*LEN_CASE +5*LEN_CASE//10, ORD*LEN_CASE +5*LEN_CASE//10),Point(ABS*LEN_CASE +6*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +4*LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),Point(ABS*LEN_CASE +5*LEN_CASE//10, ORD*LEN_CASE +5*LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +2*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),RADIUS,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +4*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),RADIUS,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +6*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),RADIUS,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +8*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),RADIUS,color)


def display_queen(ABS,ORD,color):
    """Displays queen"""

    RADIUS = LEN_CASE//4

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//3, ORD*LEN_CASE +LEN_CASE//2),RADIUS,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +2*LEN_CASE//3, ORD*LEN_CASE +LEN_CASE//2),RADIUS,color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//5, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +4*LEN_CASE//5, ORD*LEN_CASE +2*LEN_CASE//5),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//7, ORD*LEN_CASE +LEN_CASE//2),Point(ABS*LEN_CASE +4*LEN_CASE//7, ORD*LEN_CASE +17*LEN_CASE//20),color)


def display_knight(ABS,ORD,color):
    """Displays knight"""

    if color == blanc:
        opposite = noir
    else:
        opposite = blanc

    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//2),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//2),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +7*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +9*LEN_CASE//20),Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//2),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//2),Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +9*LEN_CASE//20),Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2),color)
    affiche_triangle_plein(Point(ABS*LEN_CASE +6*LEN_CASE//10, ORD*LEN_CASE +7*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//10, ORD*LEN_CASE + 7*LEN_CASE//10),Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +6*LEN_CASE//10),LEN_CASE//25,opposite)


def display_config_panel(G):
    """Shows meter, change color, timer, numer of piece.."""

    affiche_rectangle_plein(Point(LEN_GRID,0),Point(LEN_GAME,LEN_GRID),CONFIG_COLOR3)


def display_piece_selection(G):
    """Draw a box around selectedSquare"""

    if G.selectedSquare:
        affiche_rectangle(Point(G.selectedSquare[0]*LEN_CASE,G.selectedSquare[1]*LEN_CASE),Point((G.selectedSquare[0]+1)*LEN_CASE,(G.selectedSquare[1]+1)*LEN_CASE),rouge,5)


def display_valid_squ(G):
    """Draw a box around validSquares"""

    if G.selectedSquare:
        for i in range(len(G.validSquares)):

            ABS = G.validSquares[i][0]
            ORD = G.validSquares[i][1]
            affiche_rectangle(Point(ABS*LEN_CASE,ORD*LEN_CASE), Point((ABS+1)*LEN_CASE,(1+ORD)*LEN_CASE),ACTIVE_SQU_COLOR,5)


def display_game(G):
    """ Dispalys all game components"""

    display_panel()
    display_config_panel(G)
    display_valid_squ(G)
    display_piece(G,P)
    display_piece_selection(G)
    affiche_tout()




### VII MAIN ###

init_fenetre(LEN_GAME,LEN_GRID,"Chess Game")
affiche_auto_off()

P = init_piece()

PAWN_W = (P.color[0], P.type[0])
PAWN_B = (P.color[1], P.type[0])

ROOK_W = (P.color[0], P.type[1])
ROOK_B = (P.color[1], P.type[1])

KNIGHT_W = (P.color[0], P.type[2])
KNIGHT_B = (P.color[1], P.type[2])

BISHOP_W = (P.color[0], P.type[3])
BISHOP_B = (P.color[1], P.type[3])

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
                G.selectedSquare = ()


    # nothing if not on panel

    display_game(G)
attendre_echap()
