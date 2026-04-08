import numpy as np

def get_bitplanes(img):
    planes = []
    for i in range(8):
        planes.append((img >> i) & 1)
    return planes


def reconstruct_image(planes):
    img = np.zeros_like(planes[0], dtype=np.uint8)

    for i in range(8):
        shifted = (planes[i].astype(np.uint8) << i).astype(np.uint8)
        img = img | shifted   # avoid inplace |=

    return img
