import os
import cv2
import numpy as np
from PIL import Image
from pdf2image import convert_from_path


class ImageLoader:
    def carregar(self, caminho_arquivo):
        extensao = os.path.splitext(caminho_arquivo)[1].lower()

        if extensao == ".pdf":
            paginas = convert_from_path(caminho_arquivo, dpi=300)
            imagem = np.array(paginas[0])
            return cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)
        else:
            imagem = cv2.imread(caminho_arquivo)

        if imagem is None:
            raise ValueError("Erro ao carregar imagem ou caminho inválido.")

        return imagem