#################################
#       ROSSIGNOL BENJAMIN4
# Mini-Projet ISN & NSI
#        OTHELL
#    SOMMAIRE
#    1 Constantes, class
#    2 Initialisation
#    3 Utilitaires
#    4 Pose d'un pion
ombre de cases dans un coté de la grille (nbr pair)
LARGEUR_GRILLE = 600                             # Largeur de la grille en pixels
LARGEUR_CASE = LARGEUR_GRILLE // TAILLE_GRILLE   # Largeur d'une case en pixels
CENTRE_CASE = LARGEUR_CASE // 2                  # Centre d'un case en pixels
RAYON_PION = LARGEUR_CASE // 3                   # Largeur d'un pion en pixels
EPAISSEUR_PION = 2                               # Epaisseur d'un pion en pixels
COULEUR_PLATEAU = couleur(51,102,0)              # Couleur princiale du plateau de jeu
COULEUR_GRILLE = noir                            # Couleur de la grille


# Constantes du panneau d'information
LARGEUR_PANNEAU_INFORMATION = 200                # Largeur du panneau d'infomation en pixels
RAYON_INFORMATION = 75                           # Largeur d'un pion de sélection en pixels
EPAISSEUR_INFORMATION = 10                       # Epaisseur du panneau d'information en pixels


                                                 # Centre du pion d'information noir
CENTRE_INFORMATION_NOIR=Point(LARGEUR_GRILLE+LARGEUR_PANNEAU_INFORMATION//2,LARGEUR_GRILLE//4)

                                                 # Centre du pion d'information blanc
CENTRE_INFORMATION_BLANC=Point(LARGEUR_GRILLE+LARGEUR_PANNEAU_INFORMATION//2,LARGEUR_GRILLE//2+LARGEUR_GRILLE//4)
COULEUR_ACTIVE_GRIS = couleur(125,125,125)       # Couleur du cercle autour du joueur actif
COULEUR_PANNEAU = couleur(51,51,102)             # Couleur du panneau d'information


# Constantes de configuration du jeu
PREMIER_JOUEUR = NOIR


#       1.2 CLASS

class Jeu():
    """
    Contient toutes les informations du plateau de jeu de l'othello :
        - grille[i][j] : case (i,j) du plateau, valeur AUCUN ou BLANC ou NOIR
        - joueurActif : le joueur actif sur le plateau
    """

    __slots__ = (
        "grille",
        "joueurActif"
    )


    def __init__(self):
        """ la case(0,0) est la case inférieure gauche du plateau """

        self.grille = [ [AUCUN] * TAILLE_GRILLE for i in range(TAILLE_GRILLE) ]
        self.joueurActif = PREMIER_JOUEUR


# Liste des directions possibles autour d'une case
DIRECTIONS = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]



##########################################################
#        2 INITIALISATION
##########################################################

def init_jeu():
    """ initialisation du jeu :
        return : J avec un plateau de jeu initialisé pour une partie d'othello
    """

    J = Jeu()   # Crée un jeu J

    # Place des pions noirs et blancs au milieu du plateau
    J.grille[TAILLE_GRILLE//2][TAILLE_GRILLE//2-1] = NOIR
    J.grille[TAILLE_GRILLE//2-1][TAILLE_GRILLE//2] = NOIR
    J.grille[TAILLE_GRILLE//2-1][TAILLE_GRILLE//2-1] = BLANC
    J.grille[TAILLE_GRILLE//2][TAILLE_GRILLE//2] = BLANC
    return J



##########################################################
#        3 UTILITAIRES
##########################################################

def adversaire(joueur):
    """ Renvoie BLANC si le joueur est NOIR et inversement """

    # Si le joueur est noir, renvoie blanc
    if joueur == NOIR :
        J.joueurActif = BLANC

    # Si le joueur est blanc, renvoie noir
    if joueur == BLANC:
        J.joueurActif = NOIR



def get_abscisse(clic):
    """ Renvoie l'abscisse (i) de la case dans laquelle on a cliqué (les coordonnées de clic sont en pixels) """

    abs = clic.x//LARGEUR_CASE
    return abs


def get_ordonnee(clic):
    """ Renvoie l'ordonnée (j) de la case dans laquelle on a cliqué (les coordonnées de clic sont en pixels) """

    ord = clic.y//LARGEUR_CASE
    return ord



##########################################################
#        4 POSE D'UN PION
##########################################################

def pose_pion(J,i,j):
    """ pose d'un pion dans la case(i,j) de la couleur du joueur actif"""

    J.grille[i][j] = J.joueurActif


def retourne_pion(J,i,j):
    """ Retourne tous les pions mangés dans toutes les directions """
    ldv=liste_direction_valide(J,i,j)
    for k in range (len(ldv)):
        retourne_pion_pour_direction(J,i,j,ldv[k])


def retourne_pion_pour_direction(J,i,j,direction):
    """ Retourne tous les pions dans une direction """

    dirx=direction[0]                   # Coordonnée x de la liste_direction_valide
    diry=direction[1]                   # Coordonnée y de la liste_direction_valide
    if est_pos_valide(i+dirx,j+diry):   # Si la case est valide

        k=1

        while J.grille[i+dirx*k][j+diry*k] == couleur_adversaire(J.joueurActif):

                                        # Tant que la case est de couleur adverse, la case devient de la couleur du joueur actif

            J.grille[i+dirx*k][j+diry*k] = J.joueurActif
            k=k+1


def case_valide(J,i,j):
    """ Vérifie si un pion peut être posée sur la case"""

    condition=False
                                        # Si il n'y a pas de pions sur la case est qu'il y a au moins une direction valide, alors la case est valide
    if J.grille[i][j] == AUCUN and len(liste_direction_valide(J,i,j)) !=0:

        condition=True

    return condition

def liste_direction_valide(J,i,j):

    resultat = []                       # Crée une liste vide resultat
    for l in range (len(DIRECTIONS)):
        if direction_valide(J,DIRECTIONS[l],J.joueurActif,i,j)==True:
                                        # Si la direction est valide, alors ajoute la direction valide dans resultat
            resultat.append(DIRECTIONS[l])
    return resultat


def direction_valide(J,direction,joueur,i,j):
    """ Vérifie si la direction permet de poser un pion sur la case"""

    condition=False
    dirx=direction[0]                   # Coordonnée x de la direction
    diry=direction[1]                   # Coordonnée y de la direction
    if est_pos_valide(i+dirx,j+diry):
        k=1
        if J.grille[i+dirx][j+diry] == couleur_adversaire(joueur):
                                        # Si le pion de la grille dans la direction est de couleur adverse

            while est_pos_valide(i+dirx*k,j+diry*k) and J.grille[i+dirx*k][j+diry*k] != AUCUN:
                                        # Tant que la direction est valide
                if J.grille[i+dirx*k][j+diry*k] == joueur:

                    condition=True

                k=k+1

    return condition

def est_pos_valide(posx,posy):
    """ Vérifie si la case est dans la grille de jeu"""
    return 0<=posx<TAILLE_GRILLE and 0<=posy<TAILLE_GRILLE


def couleur_adversaire(joueur):
    """Renvoie la couleur adverse du joueur"""
    if joueur==NOIR:
        return BLANC
    else:
        return NOIR



##########################################################
#        5 CHANGEMENT DE JOUEUR
##########################################################

def jeu_fini(J):
    """ renvoie vrai quand le jeu est fini faux sinon """

    condition=False

    if joueur_peut_jouer(J)==False:
        adversaire(J.joueurActif)
        if joueur_peut_jouer(J)==False:
            condition=True
            print("Le jeu est terminé !")

    return condition

def joueur_peut_jouer(J):
    """ Renvoie si le joueur actif peut jouer et faux sinon """
    peut_jouer = False
    for i in range (TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            if case_valide(J,i,j):
                peut_jouer=True

    return peut_jouer



##########################################################
#        6 AFFICHAGE
##########################################################

def affiche_plateau():
    """
    Affiche le plateau de jeu (uniquement le tapis vert)
    """

    # Affiche un rectangle plein de couleur COULEUR_PLATEAU
    affiche_rectangle_plein(Point(0,0),Point(LARGEUR_GRILLE,LARGEUR_GRILLE),COULEUR_PLATEAU)


def affiche_grille():
    """
    Affiche la grille sans les pions
    """

    # Affiche les lignes horizontales
    for i in range(TAILLE_GRILLE) :
        A = Point(0,i*LARGEUR_CASE)
        B = Point(LARGEUR_GRILLE,i*LARGEUR_CASE)
        affiche_ligne(A, B, COULEUR_GRILLE, 2)

    # Affiche les lignes verticales
    for i in range(TAILLE_GRILLE):
        A = Point(i*LARGEUR_CASE,0)
        B = Point(i*LARGEUR_CASE,LARGEUR_GRILLE)
        affiche_ligne(A, B, COULEUR_GRILLE, 2)


def affiche_pions(J):
    """
    Affiche sur le plateau les pions du jeu
    """
    for i in range (TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):

            # Affiche les pions blancs
            if J.grille[i][j] == BLANC:
                A=i*LARGEUR_CASE + CENTRE_CASE
                B=j*LARGEUR_CASE + CENTRE_CASE
                affiche_cercle_plein(Point(A,B),RAYON_PION,blanc)
                affiche_cercle(Point(A,B),RAYON_PION + EPAISSEUR_PION,noir,EPAISSEUR_PION)

            # Affiche les pions noirs
            elif J.grille[i][j] == NOIR:
                A=i*LARGEUR_CASE + CENTRE_CASE
                B=j*LARGEUR_CASE + CENTRE_CASE
                affiche_cercle_plein(Point(A,B),RAYON_PION,noir)
                affiche_cercle(Point(A,B),RAYON_PION + EPAISSEUR_PION,blanc,EPAISSEUR_PION)


def affiche_selection(J):
    """
    Affiche le joueur actif dans le panneau de sélection :
        Le joueur actif est le pion entouré de gris
    """

    # Affiche le panneau de sélection
    affiche_rectangle_plein(Point(LARGEUR_GRILLE,LARGEUR_GRILLE),Point(LARGEUR_GRILLE+LARGEUR_PANNEAU_INFORMATION,0),COULEUR_PANNEAU)

    # Affiche le cercle de sélection blanc
    affiche_cercle_plein(CENTRE_INFORMATION_BLANC,RAYON_INFORMATION,blanc)

    # Affiche le cercle de sélection noir
    affiche_cercle_plein(CENTRE_INFORMATION_NOIR,RAYON_INFORMATION,noir)

    # Affiche le cercle autour cercle du joueur actif du panneau d'information
    if J.joueurActif == NOIR :
        affiche_cercle(CENTRE_INFORMATION_NOIR,RAYON_INFORMATION,COULEUR_ACTIVE_GRIS,EPAISSEUR_INFORMATION)

    if J.joueurActif == BLANC :
        affiche_cercle(CENTRE_INFORMATION_BLANC,RAYON_INFORMATION,COULEUR_ACTIVE_GRIS,EPAISSEUR_INFORMATION)

def affiche_valide(J):
    """Affiche en gris les pions des cases valides"""

    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            A=i*LARGEUR_CASE + CENTRE_CASE
            B=j*LARGEUR_CASE + CENTRE_CASE
            if J.grille[i][j]==AUCUN:
                if case_valide(J,i,j)==True:
                    affiche_cercle_plein(Point(A,B),RAYON_PION + EPAISSEUR_PION,COULEUR_ACTIVE_GRIS)

def affiche_jeu(J):
    """
    Affiche toutes les composantes du jeu
    """

    affiche_plateau()
    affiche_grille()
    affiche_pions(J)
    affiche_selection(J)
    affiche_valide(J)
    affiche_tout()



##########################################################
#        7 PROGRAMME PRINCIPAL
##########################################################

init_fenetre(LARGEUR_GRILLE + LARGEUR_PANNEAU_INFORMATION,LARGEUR_GRILLE,"Othello")

affiche_auto_off()

J = init_jeu()

affiche_jeu(J)
clic = Point()

while not(jeu_fini(J)) and pas_echap():


    clic = wait_clic()
    if clic.x < LARGEUR_GRILLE:          # on est sur le plateau de jeu
        i = get_abscisse(clic)
        j = get_ordonnee(clic)
        if J.grille[i][j] == AUCUN:      # Si il n'y a aucun pion,
            if case_valide(J,i,j)==True: # Si la case est valide,
                pose_pion(J,i,j)         # Alors pose un pion
                retourne_pion(J,i,j)     # Et retourne les pions
                adversaire(J.joueurActif)
                if joueur_peut_jouer(J)==False:
                    adversaire(J.joueurActif)



    affiche_jeu(J)

attendre_echap()

