import numpy as np
from ecc.encoding import encode_message, decode_message
from ecc.ecc_crypto import encrypt, decrypt

def encrypt_bitplane(plane, PB):
    flat = plane.flatten()
    encrypted = []

    for bit in flat:
        Pm = encode_message(int(bit))
        encrypted.append(encrypt(Pm, PB))

    return encrypted, plane.shape

def decrypt_bitplane(enc_data, shape, nB):
    decrypted = []

    for C1, C2 in enc_data:
        Pm = decrypt(C1, C2, nB)
        decrypted.append(decode_message(Pm) % 2)

    return np.array(decrypted).reshape(shape)
