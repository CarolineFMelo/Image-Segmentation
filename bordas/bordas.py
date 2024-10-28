import cv2
import numpy as np

# carrega a imagem em tons de cinza
img = cv2.imread('imagem_exemplo2.jpeg', cv2.IMREAD_GRAYSCALE)

# verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem. Verifique o nome do arquivo e o caminho.")
    exit()

# aplica filtro de suavização para reduzir o ruído
img_suavizada = cv2.GaussianBlur(img, (5, 5), 1.4)

# aplica detector de bordas Canny
bordas = cv2.Canny(img_suavizada, 100, 20)

# salva as imagens
cv2.imwrite('bordas/img_original.png', img)
cv2.imwrite('bordas/img_segmentada.png', bordas)

print("Imagens salvas.")