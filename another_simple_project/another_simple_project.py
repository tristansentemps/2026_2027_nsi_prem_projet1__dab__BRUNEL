# Create a program that simulates the mystery number game.
# A player has M attemps to discover a mystery number between 0 and N,
# that was generated randomly.
# If the player finds the mystery number or fails after M attempts, the game is over
# and the program will ask the player if he wants to go for another round.
# The program finishes only if the player said so by typing some "quitting" word
# (that is to say a text that is in the "quitting_words" list).

from outils import *

def jouer_au_jeu_mystere ():
    N = int (demander_borne_sup ())
    mystery_number = choose_a_random_number_entre_0_et_N (N)
    M = int (demander_max_attempts ())
    nbre_attemps = 1
    while nbre_attemps <= M:
        print (f"tentative n° {nbre_attemps}")
        chosen_number = int (choisir_un_nombre_entre_0_et_N (N))
        if chosen_number < mystery_number:
            print ("Trop petit !\n")
        elif chosen_number > mystery_number:
            print ("Trop grand !\n")
        else:
            afficher_bravo (mystery_number, nbre_attemps)
            saute_des_lignes (1)
            return 0
        nbre_attemps += 1
    if nbre_attemps > M:
        afficher_dommage_text (mystery_number, M)
    
def play_and_replay ():
    play_or_not = demande_sil_veut_jouer_ou_pas ()
    while play_or_not in playing_words:
        jouer_au_jeu_mystere ()
        play_or_not = demande_sil_veut_rejouer_ou_pas ()
    quitter_le_jeu ()

dis_bonjour ()
play_and_replay ()
dis_au_revoir ()




