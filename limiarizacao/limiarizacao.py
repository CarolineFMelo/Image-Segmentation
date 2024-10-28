import cv2
import numpy as np

# carrega a imagem em escala de cinza
img = cv2.imread('imagem_exemplo2.jpeg', 0)

# verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem. Verifique o nome do arquivo e o caminho.")
    exit()

# aplica limiarizazao
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
 
# salva as imagens
titles = ['limiarizacao/img_original.png', 'limiarizacao/img_segmentada.png', 'limiarizacao/img_otsu.png', 'limiarizacao/img_adaptada.png', 'limiarizacao/img_gaussiano.png']
images = [img, th1, th2, th3, th4]

for i in range(5):
    cv2.imwrite(titles[i], images[i])

print("Imagens salvas.")