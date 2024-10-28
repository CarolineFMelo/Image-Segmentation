import cv2
import numpy as np

# carrega a imagem em escala de cinza
img = cv2.imread('imagem_exemplo.jpeg')

# verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem. Verifique o nome do arquivo e o caminho.")
    exit()

# converte imagem para o espaço de cores RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# redimensionar a imagem para 2D
pixel_values = img_rgb.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# define criterios de parada e numero de clusters (K)
criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 3

# aplica K-means
_, labels, centers = cv2.kmeans(pixel_values, k, None, criterio, 10, cv2.KMEANS_RANDOM_CENTERS)

# converte os centros para valores inteiros (cores)
centers = np.uint8(centers)

# mapea cada pixel para seu respectivo centro (cluster)
img_seg = centers[labels.flatten()]

# redimensiona a imagem segmentada para a forma original
img_seg = img_seg.reshape(img_rgb.shape)

# salva as imagens
cv2.imwrite('clusterizacao/img_original.png', img)
cv2.imwrite('clusterizacao/img_segmentada.png', img_seg)

print("Imagens salvas.")