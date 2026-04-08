from ecc.curve import *
from ecc.ecc_crypto import *
from image.bitplane import *
from image.perceptual import *
from image.dct_selective import *
from utils.image_io import *
import os 
from utils.metrics import compute_psnr, compute_ssim
from utils.plot import show_comparison


os.makedirs("outputs", exist_ok=True)
# Load image
img = load_gray("inputs/cameraman.png")

# Key generation
nB = 7
PB = scalar_mult(nB, G)

# -------- PERCEPTUAL ENCRYPTION --------
planes = get_bitplanes(img)

enc7, shape = encrypt_bitplane(planes[6], PB)
enc8, _ = encrypt_bitplane(planes[7], PB)

planes[6] = decrypt_bitplane(enc7, shape, nB)
planes[7] = decrypt_bitplane(enc8, shape, nB)

reconstructed = reconstruct_image(planes)
save_image("outputs/perceptual.png", reconstructed)

# -------- SELECTIVE ENCRYPTION --------
enc_img = process_blocks(img, PB, nB, mode="encrypt")
save_image("outputs/selective.png", enc_img)


# -------- EVALUATION --------

psnr_per = compute_psnr(img, reconstructed)
ssim_per = compute_ssim(img, reconstructed)

psnr_sel = compute_psnr(img, enc_img)
ssim_sel = compute_ssim(img, enc_img)

print("\n--- Evaluation Metrics ---")
print(f"Perceptual Encryption: PSNR = {psnr_per:.4f}, SSIM = {ssim_per:.4f}")
print(f"Selective Encryption:  PSNR = {psnr_sel:.4f}, SSIM = {ssim_sel:.4f}")

# Save comparison plot
show_comparison(img, reconstructed, enc_img)
