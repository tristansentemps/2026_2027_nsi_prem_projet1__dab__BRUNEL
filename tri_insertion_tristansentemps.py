
def creer_liste():
    """Crée la liste de nombres à trier."""
    liste = [4545, 1567498,25,2758,258,96,9,]
    return liste


def trouver_position(liste, nombre, i):
    """Trouve la position où placer le nombre."""
    while i >= 0 and liste[i] > nombre:
        i = i - 1
    return i + 1


def decaler(liste, position, i):
    """Décale les nombres vers la droite."""
    while i >= position:
        liste[i + 1] = liste[i]
        i = i - 1


def tri_insertion(liste):
    """Trie la liste dans l'ordre croissant."""
    for i in range(1, len(liste)):
        nombre = liste[i]

        position = trouver_position(liste, nombre, i - 1)

        decaler(liste, position, i - 1)

        liste[position] = nombre

    return liste


def afficher(liste):
    """Affiche la liste."""
    print(liste)


def programme_principal():
    liste = creer_liste()

    print("Liste avant le tri :")
    afficher(liste)

    tri_insertion(liste)

    print("Liste après le tri :")
    afficher(liste)


programme_principal()
