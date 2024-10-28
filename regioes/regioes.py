import cv2
import numpy as np

# checa os criterios de similaridade entre vetores de cores
def criterio_similaridade(pixel1, pixel2, limiar):
    return abs(int(pixel1) - int(pixel2)) < limiar

# faz o crescimento de regiões para imagens coloridas
def crescimento_regiao(img, sementes, limiar):
    linhas, colunas= img.shape
    img_segmentada = np.zeros_like(img)
    visitados = np.zeros((linhas, colunas), dtype=bool)
    lista_pontos = []

    for semente in sementes:
        lista_pontos.append(semente)
        visitados[semente] = True

    while lista_pontos:
        x, y = lista_pontos.pop(0)
        img_segmentada[x, y] = 255

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            novo_x, novo_y = x + dx, y + dy

            if 0 <= novo_x < linhas and 0 <= novo_y < colunas:
                if not visitados[novo_x, novo_y] and criterio_similaridade(img[x, y], img[novo_x, novo_y], limiar):
                    visitados[novo_x, novo_y] = True
                    lista_pontos.append((novo_x, novo_y))

    return img_segmentada

# carrega a imagem em tons de cinza
img = cv2.imread('imagem_exemplo2.jpeg', 0)

# verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem. Verifique o nome do arquivo e o caminho.")
    exit()

# define sementes iniciais
sementes = [(100, 150), (200, 250)]

# define limiar de similaridade
limiar = 9

# aplica o crescimento de regiões
img_segmentada = crescimento_regiao(img, sementes, limiar)

# salva as imagens
cv2.imwrite('regioes/img_original.png', img)
cv2.imwrite('regioes/img_segmentada.png', img_segmentada)

print("Imagens salvas.")