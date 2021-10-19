import math
import string

def toBinary(a):
    result = ''
    result = result.join(format(ord(c), 'b') for c in a)
    return result