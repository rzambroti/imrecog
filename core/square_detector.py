import cv2
from utils.geometry import rectangles_overlap
from datetime import datetime


class SquareDetector:
    def __init__(self, gray_thresh=130, ink_thresh=145):
        self.gray_thresh = gray_thresh
        self.ink_thresh = ink_thresh

    def detectar(self, imagem_colorida):
        imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

        nome_gray = f"./data/result/gray_{self._timestamp()}.jpg"
        cv2.imwrite(nome_gray, imagem_cinza)

        _, binaria = cv2.threshold(imagem_cinza, self.gray_thresh, 255, cv2.THRESH_BINARY_INV)
        nome_bin = f"./data/result/bin_{self._timestamp()}.jpg"
        cv2.imwrite(nome_bin, binaria)

        contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        quadrados = []
        for c in contornos:
            x, y, w, h = cv2.boundingRect(c)
            if 20 < w < 60 and 20 < h < 60 and abs(w - h) < 10:
                recorte = imagem_cinza[y:y+h, x:x+w]
                media = cv2.mean(recorte)[0]

                if media < self.ink_thresh:
                    novo = (x, y, w, h)
                    if not any(rectangles_overlap(novo, existente) for existente in quadrados):
                        quadrados.append(novo)

        return sorted(quadrados, key=lambda b: (b[1], b[0]))

    def _timestamp(self):
        return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")