"""
Rétroaction :
Logique algorithmique :                 5/5 (partiellement donné)
Fonctionnement du programme python :    4/5 (il manque des affichages entre chaque tour dans la boucle)
Documentation :                         2/2 (fournie)
Total :                                 11/12
"""
import random

def choisir_mot(liste_mots):
    """
    Choisit un mot au hasard dans la liste de mots.
    :param liste_mots: Liste de mots
    :return: Le mot choisi
    """
    return random.choice(liste_mots)

def afficher_mot(mot_cache):
    """
    Affiche l’état actuel du mot (avec lettres et tirets bas).
    :param mot_cache: mot caché avec lettres et tirets
    :return: None
    """
    print("Mot actuel:", " ".join(mot_cache))

def demander_lettre(lettres_tentees):
    """
    Permet d'entrer une lettre valide (Une lettre qui n'a pas déjà été entrée
    qui est alphabétique et de longueur = 1)
    Affiche des messages pour orienter le joueur.
    :param lettres_tentees: Toutes les lettres déjà entrées auparavant
    :return: La lettre entrée valide.
    """
    while True:
        lettre = input("\nPropose une lettre: ").lower()

        if len(lettre) != 1 or not lettre.isalpha():
            print("Entrer une seule l'ettre de l'alphabet. ")
        elif lettre in lettres_tentees:
            print("Tu as déja essayer cette lettre. ")
        else:
            lettres_tentees.append(lettre)
            return lettre

def maj_mot_cache(mot_secret, mot_cache, lettre):
    """
    Met à jour le mot caché avec la lettre trouvée.
    :param mot_secret: Le mot secret
    :param mot_cache: Le mot caché
    :param lettre: La lettre trouvée
    :return: None
    """
    for i in range(len(mot_secret)):
        if mot_secret[i] == lettre:
            mot_cache[i] = lettre

def verifier_lettre(mot_cache, mot_secret, lettre, vies):
    """
    Vérifie si la lettre est dans le mot ou non. Dans le cas positif,   affiche un message
    de bon coup et met à jour le mot caché en révélant les occurrences de la lettre dans le mot
    Dans le cas négatif, diminue les vies et affiche un message à l'utilisateur
    :param mot_cache: Mot caché
    :param mot_secret: Mot secret
    :param lettre: Lettre à vérifier
    :param vies: le nombre de vies restant
    :return: le nombre de vies restant
    """
    if lettre in mot_secret:
        print("Vous avez trouver une lettre! ")
        maj_mot_cache(mot_secret, mot_cache, lettre)
    else:
        vies -= 1
        print("Mauvaise lettre. Il te reste", vies, "vies.")
    return vies


def mot_trouve(mot_cache):
    """
    Retourne True si le mot est entièrement découvert
    :param mot_cache: mot caché
    :return: True si le mot est découvert, False sinon
    """
    return "_" not in mot_cache
def jouer():
    """Boucle principale du jeu du pendu."""
    liste_mots = ["python", "programmation", "ordinateur", "pendu", "liste", "etudiant"]
    mot_secret = choisir_mot(liste_mots)
    mot_cache = ["_"] * len(mot_secret)
    lettres_tentees = []
    vies = 6

    print("🎮 Bienvenue au jeu du pendu ! 🎮")
    print("Devine le mot secret :")
    afficher_mot(mot_cache)

    while vies > 0 and not mot_trouve(mot_cache):
        lettre = demander_lettre(lettres_tentees)
        vies = verifier_lettre(
            mot_cache,
            mot_secret,
            lettre,
            vies
        )
    afficher_mot(mot_cache)                     # Ces 2 ligne doivent être décalées vers la droite
    print("Lettre tentées:", lettres_tentees)   # pour être dans la boucle.
    if mot_trouve(mot_cache):
        print("\n Tu as trouver le mot!", mot_secret)
    else:
        print("\n Tu as perdu. ")
        print("Le mot était", mot_secret)


    # while vies > 0 and not mot_trouve(mot_cache):
    # À compléter


# Lancer le jeu
jouer()


