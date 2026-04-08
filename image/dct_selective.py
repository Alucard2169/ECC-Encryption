import numpy as np
from scipy.fftpack import dct, idct
from ecc.encoding import encode_message, decode_message
from ecc.ecc_crypto import encrypt, decrypt

def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

def process_blocks(img, PB, nB, mode="encrypt"):
    h, w = img.shape
    out = np.zeros_like(img, dtype=float)

    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = img[i:i+8, j:j+8]
            d = dct2(block)

            if mode == "encrypt":
                dc = int(d[0,0])
                Pm = encode_message(dc)
                C1, C2 = encrypt(Pm, PB)
                d[0,0] = (d[0,0] % 50)  # simulate hiding

            else:
                d[0,0] = 128  # dummy restore

            out[i:i+8, j:j+8] = idct2(d)

    return np.clip(out, 0, 255).astype(np.uint8)
