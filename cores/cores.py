import cv2
import numpy as np

# carrega a imagem
img = cv2.imread('imagem_exemplo.jpeg')

# converte a imagem da escala RGB para HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# remove ruídos
img_blur = cv2.medianBlur(img_hsv, 10)

# define os limites superior e inferior de cor
inferior = np.array([33, 137, 50])
superior = np.array([50, 245, 245])

# define a máscara, região que será segmentada
mascara = cv2.inRange(img_blur, inferior, superior)

# aplica máscara na imagem original
img_final = cv2.bitwise_and(img, img, mask = mascara)

# salva as imagens
cv2.imwrite('cores/img_original.png', img)
cv2.imwrite('cores/img_hsv.png', img_hsv)
cv2.imwrite('cores/img_blur.png', img_blur)
cv2.imwrite('cores/img_mask.png', mascara)
cv2.imwrite('cores/img_segmentada.png', img_final)

print("Imagens salvas.")