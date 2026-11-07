import sys
import random

from data import * 

def saute_des_lignes (m):
    for i in range (m):
        print ("\n")

def dis_bonjour ():
    print (welcome_text)

def dis_au_revoir ():
    print (bye_bye_text)

def demande_sil_veut_jouer_ou_pas ():
    play_or_not = input (text_to_ask_to_play)
    return play_or_not

def demande_sil_veut_rejouer_ou_pas ():
    play_or_not = input (text_to_ask_to_replay)
    return play_or_not

def afficher_bravo (n, m):
    texte = text_bravo + f"{n} en {m} tentatives."
    print (texte)

def afficher_dommage_text (n, m):
    texte = text_dommage + f"{n} en moins de {m} tentatives."
    print (texte)

def demander_un_entier (mini, maxi, text):
    while True:
        n = input (text)
        if n.isdigit ():
            if int (n) < mini or int (n) > maxi:
                print (text)
            else:
                return int (n)
        else:
            print (text)
    
def demander_borne_sup ():
    n = demander_un_entier (10, 10000, text_demander_borne_sup)
    return n

def choose_a_random_number_entre_0_et_N (N):
    n = random.randint (0, N)
    return n

def demander_max_attempts ():
    n = demander_un_entier (1, 10, text_demander_max_attemps)
    return n

def choisir_un_nombre_entre_0_et_N (N):
    n = demander_un_entier (0, N, text_demander_entier_entre_0_et_N + str (N))
    return n
        
def quitter_le_jeu ():
    print (bye_bye_text)
    sys.exit (0)
    
    
