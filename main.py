import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_avatar_effect(image):
    # Führe eine bilaterale Filterung durch
    bilateral_filtered_image = cv2.bilateralFilter(image, 6, 75, 75)

    # Konvertiere das Bild in Graustufen
    gray_image = cv2.cvtColor(bilateral_filtered_image, cv2.COLOR_BGR2GRAY)

    # Wende den Stil an (Comic-Effekt)
    cartoon_image = cv2.stylization(bilateral_filtered_image, sigma_s=150, sigma_r=0.25)

    return cartoon_image

def image_to_avatar(input_image_path):
    # Lade das Bild
    image = cv2.imread(input_image_path)

    # Überprüfe, ob das Bild erfolgreich geladen wurde
    if image is None:
        print(f"Fehler beim Laden des Bildes: {input_image_path}")
        return

    # Wende den Avatar-Effekt an
    avatar_image = apply_avatar_effect(image.copy())

    # Setze die Größe des Bildes für die Anzeige
    plt.figure(figsize=(25, 8))

    # Zeige das Originalbild und das Bild mit dem Avatar-Effekt an
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Originalbild')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(avatar_image, cv2.COLOR_BGR2RGB))
    plt.title('Avatar-Effekt')

    plt.show()

# Beispielaufruf
image_to_avatar('bild.jpg')
