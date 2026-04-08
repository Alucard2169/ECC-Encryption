from ecc.curve import *

def encode_message(m):
    x = m
    while True:
        rhs = (x**3 + a*x + b) % p
        y = pow(rhs, (p+1)//4, p)
        if (y*y) % p == rhs:
            return (x, y)
        x += 1

def decode_message(P):
    return P[0]
