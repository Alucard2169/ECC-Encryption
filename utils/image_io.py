import cv2

def load_gray(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)

def save_image(path, img):
    cv2.imwrite(path, img)
