########## DISCLAMER ############

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
CIRCLE_RAY = 50

# Game Colors

PANEL_COLOR1 = couleur(130, 35, 1)        # brown
PANEL_COLOR2 = couleur(225, 224, 163)     # beige
CONFIG_COLOR3 = couleur(170,100,70)       # ligth brown
ACTIVE_SQU_COLOR = couleur(125, 125, 150) # grey
SHADOW_1 = couleur(64,18,0)               # dark brown
SHADOW_2 = couleur(206,201,104)           # dark beige
CIRCLE_SHADOW_2 = couleur(156,153,52)     # for the display_valid_squ


# Game Constants

NONE = 0
WHITE = 1
BLACK = 2

PAWN = 0
ROOK = 1
KNIGHT = 2
BISHOP = 3
QUEEN = 4
KING = 5

PAWN_DIR_W = ((0,1),(-1,1),(1,1))                                       # List of all white pawn vectorial possible moves
PAWN_DIR_B = ((0,-1),(-1,-1),(1,-1))                                    # List of all black pawn vectorial possible moves
ROOK_DIR = ((-1,0),(0,1),(1,0),(0,-1))                                  # List of all rook vectorial possible moves
KNIGHT_DIR = ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2))  # List of all knight vectorial possible moves
BISHOP_DIR = ((-1,-1),(-1,1),(1,1),(1,-1))                              # List of all bishop vectorial possible moves
QUEEN_DIR = BISHOP_DIR + ROOK_DIR                                       # List of all queen vectorial possible moves (Bishop + rook ones)
KING_DIR = QUEEN_DIR                                                    # List of all king vectorial possible moves (Same as queen)

# List of all directions for each piece
MOVE_LIST = {

    "PAWN_W": PAWN_DIR_W,
    "PAWN_B": PAWN_DIR_B,
    ROOK: ROOK_DIR,
    KNIGHT: KNIGHT_DIR,
    BISHOP: BISHOP_DIR,
    QUEEN: QUEEN_DIR,
    KING: KING_DIR
}

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



### II INITIALIZATION ###

def init_piece():
    """Initialize class Piece"""

    P = Piece()

    return P


def init_game ():
    """Game loaded with class game + all pieces"""

    # Initialize class game
    G = Game()

    # Places all games pieces on the grid :
    # loops to create pieces on both sides

    for column in range (NBR_SQU):
        G.grid[column][1] = (WHITE, PAWN) #PAWN_W
        G.grid[column][6] = (BLACK, PAWN) #PAWN_B

    for column in range (0, 8, 7):
        G.grid[column][0] = (WHITE, ROOK) #ROOK_W
        G.grid[column][7] = (BLACK, ROOK) #ROOK_W

    for column in range (1, 8, 5):
        G.grid[column][0] = (WHITE, KNIGHT) #KNIGHT_W
        G.grid[column][7] = (BLACK, KNIGHT) #KNIGHT_B

    for column in range (2, 8, 3):
        G.grid[column][0] = (WHITE, BISHOP) #BISHOP_W
        G.grid[column][7] = (BLACK, BISHOP) #BISHOP_B

    G.grid[3][0] = (WHITE, QUEEN) #QUEEN_W
    G.grid[3][7] = (BLACK, QUEEN) #QUEEN_B

    G.grid[4][0] = (WHITE, KING) #KING_W
    G.grid[4][7] = (BLACK, KING) #KING_B

    return G


def end_game(G):
    """End of the game if Mate"""

    pass




### III UTILITIES ###

def get_abs(clic):
    """Return square abs in grid"""

    return clic.x // LEN_CASE


def get_ord(clic):
    """Return square ord in grid"""

    return clic.y // LEN_CASE


def what_is_piece(G, ABS, ORD):
    """Return piece type and color"""

    return G.grid[ABS][ORD]


def change_maj_piece_color(COLOR):
    """Change color in CAPITAL letters into color in lowercase letters (for display color)"""

    if COLOR == WHITE:
        return blanc
    else:
        return noir


def piece_display_type(TYPE):
    """Check what piece it is and return display_'Piece name'"""

    if TYPE == PAWN:
        return display_pawn
    elif TYPE == ROOK:
        return display_rook
    elif TYPE == KNIGHT:
        return display_knight
    elif TYPE == BISHOP:
        return display_bishop
    elif TYPE == QUEEN:
        return display_queen
    else:
        return display_king


def promotion_type(G, TYPE):
    """associate the return type to the game type"""

    if TYPE == "ROOK":
        return ROOK
    elif TYPE == "KNIGHT":
        return KNIGHT
    elif TYPE == "BISHOP":
        return BISHOP
    elif TYPE == "QUEEN":
        return QUEEN


def is_in_grid(ABS, ORD):
    """Returns True if square is still in the game grid"""

    return 0<=ABS<NBR_SQU and 0<=ORD<NBR_SQU


def is_in_valid_square(G):
    """"Check if arrivalSquare is in the validSquare list"""

    for square in G.validSquares:
        if square == G.arrivalSquare:
            return True

    return False


def are_same_color(G, ABS, ORD):
    """Returns True if selectedPiece's color and entryPiece's color are the same"""

    return what_is_piece(G, G.selectedSquare[0], G.selectedSquare[1])[0] == what_is_piece(G, ABS, ORD)[0]


def change_player(G):
    """Changes the Active Player"""

    if G.activePlayer == BLACK:
        G.activePlayer = WHITE
    else:
        G.activePlayer = BLACK


def empty_pos(G, ABS, ORD):
    """Returns True if the pos is empty"""

    return G.grid[ABS][ORD] == NONE


def is_pawn_promotion(G):
    """send you to promotion if your pawn is at the grid's end """

    for column in range (NBR_SQU):
        if G.grid[column][7] == (WHITE, PAWN) or G.grid[column][0] == (BLACK, PAWN): #if pawn is on either side
            return True

    return False


def is_in_check_piece(G, ABS, ORD):
    """Check if opposite piece makes king in check"""

    PIECE = what_is_piece(G, ABS, ORD)
    KING = where_is_same_king(G, PIECE[0])

    store_valid_square(G, ABS, ORD)

    if (ABS, ORD) in G.validSquares:
        return True

    return False


def where_is_same_king(G, COLOR):
    """Return position of entry color king"""

    for ABS in range(NBR_SQU):
        for ORD in range(NBR_SQU):
            if  G.grid[ABS][ORD] == (COLOR, KING):
                return (ABS, ORD)



### IV DROP PIECES ###

def select_piece(G, ABS, ORD):
    """Stores the piece you click on in G.selectedSquare and display all squares this Piece can go to"""

    G.selectedSquare = (ABS, ORD)
    store_valid_square(G, ABS, ORD)


def store_arrivalSquare(G, ABS, ORD):
    """After 2nd click, stores square in G.arrivalSquare"""

    G.arrivalSquare = (ABS, ORD)


def drop_piece(G, ABS, ORD):
    """Drops the selectedSquare Piece on arrivalSquare then deletes it from selectedSquare"""

    G.grid[G.arrivalSquare[0]][G.arrivalSquare[1]] = what_is_piece(G, G.selectedSquare[0], G.selectedSquare[1])

    if is_pawn_promotion(G):
        promotion(G)

    delete_piece(G, G.selectedSquare[0], G.selectedSquare[1])  # take off the piece (1st piece)


def delete_piece(G, ABS, ORD):
    """Deletes piece after moving"""

    G.grid[ABS][ORD] = NONE
    unselect_piece(G)


def unselect_piece(G):
    """Unselect piece after clicking on other square"""

    G.selectedSquare = ()
    G.validSquares = []

def store_valid_square(G, ABS, ORD):
    """Empty the G.validSquares list and reupdates it with the current selectedPiece"""

    PIECE = what_is_piece(G, ABS, ORD) # Stores selectedPiece color/type

    if PIECE[1] == PAWN:
        store_move_pawn(G, ABS, ORD)

    else:
        store_move_piece(G, ABS, ORD)


def store_move_piece(G, ABS, ORD):
    """Store all the selectedPiece validSquares (except Pawn)"""

    PIECE = what_is_piece(G, ABS, ORD)
    DIR_LIST = MOVE_LIST[PIECE[1]]

    if PIECE[1] == KING or PIECE[1] == KNIGHT:
        LOOP = False
    else:
        LOOP = True

    for LST_INDEX in DIR_LIST:
        store_move_dir(G, ABS, ORD, LST_INDEX, LOOP)


def store_move_dir(G, ABS, ORD, LST_INDEX, LOOP):
    """Stores valid positions for one direction"""

    ABS += LST_INDEX[0]
    ORD += LST_INDEX[1]
    condition = True

    while is_in_grid(ABS, ORD) and condition:

        if empty_pos(G, ABS, ORD):
            G.validSquares.append((ABS, ORD))

        else:
            if not are_same_color(G, ABS, ORD):
                G.validSquares.append((ABS, ORD))
                return G

            if are_same_color(G, ABS, ORD):
                return G

        if LOOP:
            ABS += LST_INDEX[0]
            ORD += LST_INDEX[1]
        else:
            return G


def store_move_pawn(G, ABS, ORD):
    """Stores all the pawn validSquares. Pawn has very special moves"""

    PAWN = what_is_piece(G, ABS, ORD)

    # Takes the list directions and beginning pos of pawn color
    if PAWN[0] == WHITE:
        DIR_LIST = MOVE_LIST["PAWN_W"]
        STARTING_ORD = 1
    else:
        DIR_LIST = MOVE_LIST["PAWN_B"]
        STARTING_ORD = 6

    # ABS_VECT is pawn_abs + direction vector
    ABS_VECT, ORD_VECT = ABS + DIR_LIST[0][0], ORD + DIR_LIST[0][1]


    # Diagonal move : if there is an ennemy piece
    for LST_INDEX in range(1,3):

        ABS_VECT, ORD_VECT = ABS + DIR_LIST[LST_INDEX][0], ORD + DIR_LIST[LST_INDEX][1]

        if is_in_grid(ABS_VECT, ORD_VECT) and not empty_pos(G, ABS_VECT, ORD_VECT):
                if not are_same_color(G, ABS_VECT, ORD_VECT):
                    G.validSquares.append((ABS_VECT, ORD_VECT))

    # Front move : if there is no piece 1 case in front
    ABS_VECT, ORD_VECT = ABS + DIR_LIST[0][0], ORD + DIR_LIST[0][1]
    if is_in_grid(ABS_VECT, ORD_VECT) and empty_pos(G, ABS_VECT, ORD_VECT):
        G.validSquares.append((ABS_VECT, ORD_VECT))

        # Beginning move : if there is no piece 2 cases in front. 2x the front vector
        ABS_VECT, ORD_VECT = ABS + 2*DIR_LIST[0][0], ORD + 2*DIR_LIST[0][1]
        if ORD == STARTING_ORD and empty_pos(G, ABS_VECT, ORD_VECT):
            G.validSquares.append((ABS_VECT, ORD_VECT))


def promotion(G):
    """Allow you to change your pawn's type if you arrived at the end of the grid"""

    CHOOSING_PIECE = True
    PAWN = what_is_piece(G, G.selectedSquare[0], G.selectedSquare[1])

    while CHOOSING_PIECE:
        PIECE_TYPE = input("insert which piece you want (ROOK, KNIGHT, BISHOP, QUEEN")

        if PIECE_TYPE == "ROOK" or PIECE_TYPE == "KNIGHT" or PIECE_TYPE == "BISHOP" or PIECE_TYPE == "QUEEN":
            G.grid[G.arrivalSquare[0]][G.arrivalSquare[1]] = (PAWN[0], promotion_type(G, PIECE_TYPE))
            return G

        else :
            print("Please try again, it's not a valid piece")


def is_in_check(G):
    """Check if king is in ... check"""


    for ABS in range(NBR_SQU):
        for ORD in range(NBR_SQU):
            if not empty_pos(G, ABS, ORD) and not are_same_color(G, ABS, ORD):

                if is_in_check_piece(G, ABS, ORD):
                    return True

    return False


### VI DISPLAY ###

def display_panel():
    """Show the panel with 2 different colors for each case"""

    for ABS in range (NBR_SQU):
        for ORD in range (NBR_SQU):
            if ABS%2 == 0 and ORD%2 == 0 or ABS%2 != 0 and ORD%2 != 0:
            # If square abs and ord are even or if square abs and ord are odd
                affiche_rectangle_plein(Point(LEN_CASE*ABS, LEN_CASE*ORD), Point(LEN_CASE*(ABS+1), LEN_CASE*(ORD+1)), PANEL_COLOR1)

            else :
                affiche_rectangle_plein(Point(LEN_CASE*ABS, LEN_CASE*ORD), Point(LEN_CASE*(ABS+1), LEN_CASE*(ORD+1)), PANEL_COLOR2)


def display_config_panel(G):
    """Shows meter, change color,player, timer, numer of piece.."""

    affiche_rectangle_plein(Point(LEN_GRID,0), Point(LEN_GAME,LEN_GRID), CONFIG_COLOR3)
    affiche_ligne(Point(LEN_GRID,0), Point(LEN_GRID,LEN_GRID), noir, 7)

    display_two_players(G)
    display_active_player(G)

def display_two_players(G):
    """Display the 2 players with their own color"""

    # Displays "PLAYER 2"
    display_player(G, 0, noir)
    display_two()

    # Displays "PLAYER 1"
    display_player(G, 350, blanc)
    display_one()


def display_player(G, DOWN, color):
    """Displays "PLAYER" in config panel. 'DOWN' is how much pixel needs the text to be down"""

    # P
    affiche_ligne(Point(LEN_GRID+30,580-DOWN), Point(LEN_GRID+30,550-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+45,580-DOWN), Point(LEN_GRID+45,565-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+30,580-DOWN), Point(LEN_GRID+45,580-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+30,565-DOWN), Point(LEN_GRID+45,565-DOWN), color, 3)

    # L
    affiche_ligne(Point(LEN_GRID+55,580-DOWN), Point(LEN_GRID+55,550-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+55,550-DOWN), Point(LEN_GRID+70,550-DOWN), color, 3)

    # A
    affiche_ligne(Point(LEN_GRID+80,580-DOWN), Point(LEN_GRID+80,550-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+95,580-DOWN), Point(LEN_GRID+95,550-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+80,580-DOWN), Point(LEN_GRID+95,580-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+80,565-DOWN), Point(LEN_GRID+95,565-DOWN), color, 3)

    # Y
    affiche_ligne(Point(LEN_GRID+105,580-DOWN), Point(LEN_GRID+105,565-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+112,565-DOWN), Point(LEN_GRID+112,550-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+120,580-DOWN), Point(LEN_GRID+120,565-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+105,565-DOWN), Point(LEN_GRID+120,565-DOWN), color, 3)

    # E
    affiche_ligne(Point(LEN_GRID+130,580-DOWN), Point(LEN_GRID+130,550-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+130,580-DOWN), Point(LEN_GRID+145,580-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+130,565-DOWN), Point(LEN_GRID+145,565-DOWN), color, 3)
    affiche_ligne(Point(LEN_GRID+130,550-DOWN), Point(LEN_GRID+145,550-DOWN), color, 3)

    # R
    affiche_ligne(Point(LEN_GRID+155,580-DOWN),Point(LEN_GRID+155,550-DOWN),color,3)
    affiche_ligne(Point(LEN_GRID+170,580-DOWN),Point(LEN_GRID+170,565-DOWN),color,3)
    affiche_ligne(Point(LEN_GRID+155,580-DOWN),Point(LEN_GRID+170,580-DOWN),color,3)
    affiche_ligne(Point(LEN_GRID+155,565-DOWN),Point(LEN_GRID+170,565-DOWN),color,3)
    affiche_ligne(Point(LEN_GRID+155,565-DOWN),Point(LEN_GRID+170,550-DOWN),color,3)


def display_two():
    """Displays 2"""

    affiche_ligne(Point(LEN_GRID+85,510), Point(LEN_GRID+85,525), noir, 3)
    affiche_ligne(Point(LEN_GRID+115,540), Point(LEN_GRID+115,525), noir, 3)
    affiche_ligne(Point(LEN_GRID+85,540), Point(LEN_GRID+115,540), noir, 3)
    affiche_ligne(Point(LEN_GRID+115,525), Point(LEN_GRID+85,525), noir, 3)
    affiche_ligne(Point(LEN_GRID+115,510), Point(LEN_GRID+85,510), noir, 3)


def display_one():
    """Displays 1"""

    affiche_ligne(Point(LEN_GRID+100,190), Point(LEN_GRID+100,160), blanc, 3)
    affiche_ligne(Point(LEN_GRID+85,175), Point(LEN_GRID+100,190), blanc, 3)
    affiche_ligne(Point(LEN_GRID+115,160), Point(LEN_GRID+85,160), blanc, 3)


def display_active_player(G):
    """Displas which color is playing"""

    affiche_cercle_plein(Point(LEN_GRID+LEN_PANEL//2, LEN_GRID//2), CIRCLE_RAY, change_maj_piece_color(G.activePlayer))
    affiche_cercle(Point(LEN_GRID+LEN_PANEL//2, LEN_GRID//2), CIRCLE_RAY+1,ACTIVE_SQU_COLOR,5)


def display_piece(G):
    """Display all game pieces, including their color and type"""

    for ABS in range (NBR_SQU):
        for ORD in range (NBR_SQU):
            if not empty_pos(G, ABS, ORD):
                PIECE = what_is_piece(G, ABS, ORD)
                color = change_maj_piece_color(PIECE[0]) # Stores lowercase color

                # Stores the piece's name in piece_movetype. If a PAWN is on [ABS][ORD] :
                # piece_display_type(G.grid[ABS][ORD][0]) will return the text 'display_pawn'

                display_type = piece_display_type(PIECE[1])

                # function called here is actually named 'piece_"pieceName"'
                display_type(ABS, ORD, color)


def display_pawn(ABS, ORD, color):
    """Displays pawn"""

    RADIUS = LEN_CASE//6

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2+RADIUS),RADIUS-RADIUS//3,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2),RADIUS,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2-RADIUS),RADIUS+RADIUS//3,color)


def display_rook(ABS, ORD, color):
    """Displays rook"""

    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +2*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//10, ORD*LEN_CASE +2*LEN_CASE//10),Point(ABS*LEN_CASE +7*LEN_CASE//10, ORD*LEN_CASE +7*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//9, ORD*LEN_CASE +7*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +2*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +4*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +5*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +6*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +7*LEN_CASE//9, ORD*LEN_CASE +8*LEN_CASE//10),Point(ABS*LEN_CASE +8*LEN_CASE//9, ORD*LEN_CASE +9*LEN_CASE//10),color)


def display_knight(ABS, ORD, color):
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


def display_bishop(ABS, ORD, color):
    """Displays bishop"""

    RADIUS = LEN_CASE//4

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2+RADIUS),RADIUS//3,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//2, ORD*LEN_CASE +LEN_CASE//2),RADIUS,color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//10, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +9*LEN_CASE//10, ORD*LEN_CASE +3*LEN_CASE//10),color)


def display_queen(ABS, ORD, color):
    """Displays queen"""

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


def display_king(ABS,ORD,color):
    """Displays king"""

    RADIUS = LEN_CASE//4

    affiche_cercle_plein(Point(ABS*LEN_CASE +LEN_CASE//3, ORD*LEN_CASE +LEN_CASE//2),RADIUS,color)
    affiche_cercle_plein(Point(ABS*LEN_CASE +2*LEN_CASE//3, ORD*LEN_CASE +LEN_CASE//2),RADIUS,color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +LEN_CASE//5, ORD*LEN_CASE +LEN_CASE//10),Point(ABS*LEN_CASE +4*LEN_CASE//5, ORD*LEN_CASE +2*LEN_CASE//5),color)
    affiche_rectangle_plein(Point(ABS*LEN_CASE +3*LEN_CASE//7, ORD*LEN_CASE +LEN_CASE//2),Point(ABS*LEN_CASE +4*LEN_CASE//7, ORD*LEN_CASE +17*LEN_CASE//20),color)


def display_piece_selection(G):
    """Draw a box around selectedSquare"""

    if G.selectedSquare:
        affiche_rectangle(Point(G.selectedSquare[0]*LEN_CASE,G.selectedSquare[1]*LEN_CASE),Point((G.selectedSquare[0]+1)*LEN_CASE,(G.selectedSquare[1]+1)*LEN_CASE),rouge,5)

def display_valid_squ(G):
    """Draw a box around validSquares"""

    if G.selectedSquare:
        for VALID_SQU in range(len(G.validSquares)):

            ABS, ORD = G.validSquares[VALID_SQU][0], G.validSquares[VALID_SQU][1]

            CIRCLE_CENTER = Point(ABS*LEN_CASE + LEN_CASE//2,ORD*LEN_CASE + LEN_CASE//2)

            if ABS%2 == 0 and ORD%2 == 0 or ABS%2 != 0 and ORD%2 != 0:
                    # If square abs and ord are even or if square abs and ord are odd
                affiche_cercle_plein(CIRCLE_CENTER,CIRCLE_RAY//3,SHADOW_1)     # For dark brown
                affiche_cercle(CIRCLE_CENTER,CIRCLE_RAY//3,noir)

            else :
                affiche_cercle_plein(CIRCLE_CENTER,CIRCLE_RAY//3,SHADOW_2)      # For dark beige
                affiche_cercle(CIRCLE_CENTER,CIRCLE_RAY//3,CIRCLE_SHADOW_2)


def display_game(G):
    """ Dispalys all game components"""

    display_panel()
    display_config_panel(G)
    display_piece(G)
    display_piece_selection(G)
    display_valid_squ(G)

    affiche_tout()




### VII MAIN ###

init_fenetre(LEN_GAME,LEN_GRID,"Chess Game")
affiche_auto_off()

#P = init_piece()
G = init_game()

display_game(G)


while not(end_game(G)) and pas_echap():

    clic = wait_clic()
    if clic.x < LEN_GRID and clic.y < LEN_GRID: # we are on the panel

        ABS, ORD = get_abs(clic), get_ord(clic)

        if not empty_pos(G, ABS, ORD) and not(G.selectedSquare) :
            if what_is_piece(G, ABS, ORD)[0] == G.activePlayer:
                select_piece(G, ABS, ORD) # select the piece



        elif G.selectedSquare: #no piece and a piece selected before

            store_arrivalSquare(G, ABS, ORD)

            if is_in_valid_square(G):
                drop_piece(G, ABS, ORD)    # drop a piece on the case selcted (2nd clic)
                change_player(G)

            else:
                unselect_piece(G)


    # nothing if not on panel

    display_game(G)
attendre_echap()
