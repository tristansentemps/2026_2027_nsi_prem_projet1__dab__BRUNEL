from data import *
from outils import *

def ask_for_a_positive_integer ():
    """ Asking for the positive integer """
    pos_int = input (text_shown_when_asking_for_pos_int)
    while is_not_a_valid_bin_or_dec_or_hex_number (pos_int):
        if is_a_quit_command (pos_int):
            exit_from_application ()
        else:
            pos_int = input (text_shown_when_re_asking_for_pos_int)
    return pos_int

def are_consistent (pos_int, init_base):
    """ La fonction vérifie si pos_int et init_base sont compatibles """
    if could_be_a_binary_integer (pos_int): # le pos_int est un binaire
        return True  # un binaire est toujours compatible avec init_base
    elif could_be_a_decimal_integer (pos_int): # le pos_int est un décimal
        return is_decimal_base (init_base) or is_hexadecimal_base (init_base) #  init_base can be 10 or 16
    else: # le pos_int is a hexadecimal
        return is_hexadecimal_base (init_base) # init_base ne peut être que hexadécimal

def are_not_consistent (pos_int, init_base):
    return not (are_consistent (pos_int, init_base))

def ask_for_the_initial_base (pos_int):
    """ Asking for the initial base """
    init_base = input (text_shown_when_asking_for_initial_base)
    while is_not_a_valid_base (init_base) or are_not_consistent (pos_int, init_base):
        init_base = input (text_shown_when_re_asking_for_initial_base)
    return init_base

def ask_for_the_target_base ():
    """ Asking for the target base """
    target_base = input (text_shown_when_asking_for_target_base)
    while is_not_a_valid_base (target_base):
        target_base = input (text_shown_when_re_asking_for_target_base)
    return target_base

def convert_number (pos_int, initial_base, target_base):
    """ Main conversion function. 
          at this stage, pos_int and initial_base are supposed to be consistent """
    if are_the_same (initial_base, target_base):
        conv_num = pos_int
    else:
        if is_binary_base (initial_base):
            if is_decimal_base (target_base):
                conv_num = bin_to_dec (pos_int)
            else: # case of hexadecimal base
                conv_num = bin_to_hex (pos_int)
        elif is_decimal_base (initial_base):
            if is_binary_base (target_base):
                conv_num = dec_to_bin (pos_int)
            else: # case of hexadecimal base
                conv_num = dec_to_hex (pos_int)
        else:  # case of hexadecimal base
            if is_binary_base (target_base):
                conv_num = hex_to_bin (pos_int)
            else: #  case of decimal base
                conv_num = hex_to_dec (pos_int)
        return conv_num

def make_text_to_be_printed ( \
                              pos_int, \
                              initial_base, \
                              target_base, \
                              converted_number):
    """ Function that builds the conclusion text """
    text = \
        "\nLe nombre " \
        + str (pos_int) \
        + " écrit en base " \
        + str (initial_base) \
        + ", a pour conversion en base " \
        + str (target_base) \
        + " :  " \
        + str (converted_number)
    return text

def main ():
    positive_integer = ask_for_a_positive_integer ()
    initial_base = ask_for_the_initial_base (positive_integer)
    target_base = ask_for_the_target_base ()
    converted_number = \
        convert_number ( \
                            positive_integer, \
                            initial_base, \
                            target_base)
    texte = \
        make_text_to_be_printed ( \
                               positive_integer, \
                               initial_base, \
                               target_base, \
                               converted_number)
    print (texte)

def play_and_replay ():
    play = "yes"
    while play in replay_commands:
        main ()
        play = input (text_for_replaying)

# Welcoming the user
print (text_welcome)

# Asking for playing and replaying program
play_and_replay ()

# Printing "Au revoir" text
print (text_bye_bye)
