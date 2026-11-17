text_for_replaying = \
    "\n\n      Souhaitez-vous convertir un autre nombre entier ? "

text_shown_when_asking_for_pos_int = \
    "\nVeuillez entrer un entier positif en base 2, 10 ou 16: "

text_shown_when_re_asking_for_pos_int = \
    "\nLe programme n'est pas en mesure de traiter autre chose qu'un entier positif,\n" \
    + text_shown_when_asking_for_pos_int

bin_chars = \
    [1, 0, "1", "0"]

dec_chars = \
    [ \
      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \
      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' \
    ] \
    
hex_chars = \
    ['a', 'b', 'c', 'd', 'e', 'f', \
     "A", "B", "C", "D", "E", "F" \
    ]

authorized_chars = \
    dec_chars \
    + hex_chars

text_shown_when_asking_for_initial_base = \
    "\nVeuillez entrer la base dans laquelle est écrite l'entier positif\n" \
    + "précédemment renseigné (2, 10 ou 16) :  "

text_only_2_10_and_16_bases = \
    "\nVous avez entré comme base une valeur autre que 2, 10 ou 16,\n"

text_shown_when_re_asking_for_initial_base = \
    "\nL'une ou l'autre des situations suivantes s'est présentée :\n" \
    + " *) Vous avez entré une autre base que 2, 10 ou 16\n" \
    + " *) La base initiale que vous déclarez n'est pas compatible avec l'entier entré.\n" \
    + text_shown_when_asking_for_initial_base

text_shown_when_asking_for_target_base = \
    "\nVeuillez entrer la base dans laquelle sera écrite l'entier positif\n" \
    + "précédemment renseigné (2, 10 ou 16) :  "

text_shown_when_re_asking_for_target_base = \
    text_only_2_10_and_16_bases \
    + text_shown_when_asking_for_target_base

authorized_bases = \
    ['2', '10', '16']

replay_commands = \
    ["y", "yes", "Y", "go", "ok", "Yes", "on y va", "let's go", "oui", "o", "O", "Oui"]

quit_commands = \
    ["q", "Q", "quit", "Quit", "ko", "by", \
     "au revoir", "see u", "see you", "ciao", \
     "kill" , "out", "Out", "sortir", "s", "n", ]

# Dictionnaire qui fait la correspondance entre les lettres et les nombres de 10 à 15
# qui interviennent dans l'écriture des entiers hexadécimaux.
dico = \
    { \
      "0" : 0, \
      "1" : 1, \
      "2" : 2, \
      "3" : 3, \
      "4" : 4, \
      "5" : 5, \
      "6" : 6, \
      "7" : 7, \
      "8" : 8, \
      "9" : 9, \
      0 : 0, \
      1 : 1, \
      2 : 2, \
      3 : 3, \
      4 : 4, \
      5 : 5, \
      6 : 6, \
      7 : 7, \
      8 : 8, \
      9 : 9, \
      "a" : 10, \
      "b" : 11, \
      "c" : 12, \
      "d" : 13, \
      "e" : 14, \
      "f" : 15,  \
      "A" : 10, \
      "B" : 11, \
      "C" : 12, \
      "D" : 13, \
      "E" : 14, \
      "F" : 15 \
      }

xdico = \
    { \
      0 : 0, \
      1 : 1, \
      2 : 2, \
      3 : 3, \
      4 : 4, \
      5 : 5, \
      6 : 6, \
      7 : 7, \
      8 : 8, \
      9 : 9, \
      10 : "a", \
      11 : "b", \
      12 : "c", \
      13 : "d", \
      14 : "e", \
      15 : "f" \
      }

text_bye_bye = \
    "\n*********************************************************************\n" \
    + "\nJ'ai été ravi de vous aider dans vos conversions de nombres entiers... A bientôt !\n\n"

text_welcome = \
    "\nBonjour, bienvenu dans notre application de conversion " \
    + "d'entier positif en base 2, 10 ou 16 en un entier en base 2, 10 ou 16.\n" \
    + "A tout moment vous pouvez sortir de l'application en tapant " + '"q"' + " ou " + '"quit"' + "\n"
