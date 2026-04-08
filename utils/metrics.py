import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def compute_psnr(original, processed):
    return peak_signal_noise_ratio(original, processed, data_range=255)

def compute_ssim(original, processed):
    return structural_similarity(original, processed, data_range=255)
