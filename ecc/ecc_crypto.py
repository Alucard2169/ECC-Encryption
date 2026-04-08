import random
from ecc.curve import *

def encrypt(Pm, PB):
    k = random.randint(1, 100)
    C1 = scalar_mult(k, G)
    C2 = point_add(Pm, scalar_mult(k, PB))
    return C1, C2

def decrypt(C1, C2, nB):
    S = scalar_mult(nB, C1)
    return point_add(C2, point_neg(S))
