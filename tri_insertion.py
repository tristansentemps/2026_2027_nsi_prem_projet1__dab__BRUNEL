def find_right_pos (v , i):
    """ sublist v [:i-1] is supposed to be sorted.
        One determines at which position value v [i] 
        has to be insered in order to keep sublist 
        sorted.
    """
    ...

def shift_to_right (v, i, j):
    """ values from index i to index j
        are shifted to the right.
        Index j is supposed to be <= len(v) - 2
    """
    ...

def tri_insertion (v):
    for i in range (1, len (v)):
        value_to_be_inserted = v [i]
        right_pos = \
          find_right_pos (v, ..., ...)
        v = \
          shift_to_the_right (v, right_pos, i - 1)
        v [right_pos] = value_to_be_inserted

v = [11, 5, 63, 89, 45, 12]
print (tri_insertion (v))



