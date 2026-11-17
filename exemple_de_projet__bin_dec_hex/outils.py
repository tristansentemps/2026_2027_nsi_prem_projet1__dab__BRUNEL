from data import *

def is_a_valid_base (b):
    return b in authorized_bases

def is_not_a_valid_base (b):
    return not (is_a_valid_base (b))

def is_a_valid_bin_or_dec_or_hex_number (chain):
    for char in chain:
        if char not in authorized_chars:
            return False
    return True

def is_not_a_valid_bin_or_dec_or_hex_number (x):
    return not (is_a_valid_bin_or_dec_or_hex_number (x))

def are_the_same (x, y):
    return x == y

def is_binary_base (base):
    return base in [2, "2"]

def is_decimal_base (base):
    return base in [10, "10"]

def is_hexadecimal_base (base):
    return base in [16, "16"]

def could_be_a_binary_integer (pos_int):
    for i in pos_int:
        if i not in bin_chars:
            return False
    return True

def could_be_a_decimal_integer (pos_int):
    for i in pos_int:
        if i not in dec_chars:
            return False
    return True

# Basics conversion functions:   bin <--> dec <--> hex <--> bin
def base_to_dec (base, pos_int):
    """ pos_int est une chaine de caractères dont les caractères appartiennent 
          tous à authorized_chars """
    dec_num = 0
    for i in range (len (pos_int)):
        dec_num = dec_num + int (dico [pos_int [i]]) * base ** (len (pos_int) - 1 - i)
    return dec_num

def dec_to_base (pos_int, base):
    restes = ""
    quotient = int (pos_int)
    while quotient != 0:
        reste = quotient % base
        quotient = quotient // base
        restes = str (xdico [reste]) + restes
    return restes

def bin_to_dec (pos_int):
    return base_to_dec (2, pos_int)

def dec_to_hex (pos_int):
    return dec_to_base (pos_int, 16)

def bin_to_hex (pos_int):
    return dec_to_hex (bin_to_dec (pos_int))

def dec_to_bin (pos_int):
    return dec_to_base (pos_int, 2)

def hex_to_dec (pos_int):
    return base_to_dec (16, pos_int)

def hex_to_bin (pos_int):
    return dec_to_bin (hex_to_dec (pos_int))

def is_a_quit_command (chain):
    return chain in quit_commands

def exit_from_application ():
    print (text_exit)
    exit ()
