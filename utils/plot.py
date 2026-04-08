import matplotlib.pyplot as plt

def show_comparison(original, perceptual, selective):
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.imshow(original, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Perceptual Encryption")
    plt.imshow(perceptual, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Selective Encryption")
    plt.imshow(selective, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.savefig("outputs/comparison.png")
    plt.show()
