
def creer_liste():
    liste = [446,6,5,555,512,4,7,]
    return liste

def trouver_position(liste, nombre, i):
    while i >= 0 and liste[i] > nombre:
        i = i - 1
    return i + 1

def decaler(liste, position, i):
    while i >= position:
        liste[i + 1] = liste[i]
        i = i - 1

def tri_insertion(liste):
    for i in range(1, len(liste)):
        nombre = liste[i]
        position = trouver_position(liste, nombre, i - 1)
        decaler(liste, position, i - 1)
        liste[position] = nombre

    return liste

def afficher(liste):
    print(liste)

def programme_principal():
    liste = creer_liste()

    print("Liste avant :")
    afficher(liste)

    tri_insertion(liste)

    print("Liste après :")
    afficher(liste)

programme_principal()



print(1.5 +1.75+ 0.8+ 0.75+ 0.5+ 1.5+ 0.5+ 1.5 +0.5+2 )