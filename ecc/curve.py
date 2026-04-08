p = 53330939
a = 2
b = 7
G = (503152, 736)

def mod_inv(x):
    return pow(x, -1, p)

def point_add(P, Q):
    if P is None: return Q
    if Q is None: return P

    x1, y1 = P
    x2, y2 = Q

    if P == Q:
        lam = (3*x1*x1 + a) * mod_inv(2*y1) % p
    else:
        lam = (y2 - y1) * mod_inv(x2 - x1) % p

    x3 = (lam*lam - x1 - x2) % p
    y3 = (lam*(x1 - x3) - y1) % p

    return (x3, y3)

def scalar_mult(k, P):
    R = None
    while k:
        if k & 1:
            R = point_add(R, P)
        P = point_add(P, P)
        k >>= 1
    return R

def point_neg(P):
    return (P[0], (-P[1]) % p)
