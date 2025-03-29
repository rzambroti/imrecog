import cv2
from datetime import datetime

class Visualizer:
    def exibir(self, imagem, quadrados):
        imagem_cp = imagem.copy()
        fonte = cv2.FONT_HERSHEY_SIMPLEX

        for idx, (x, y, w, h) in enumerate(quadrados, 1):
            cv2.rectangle(imagem_cp, (x, y), (x + w, y + h), (0, 255, 0), 1)
            texto = str(idx)
            (tw, th), _ = cv2.getTextSize(texto, fonte, 0.6, 2)
            pos_texto = (x + w // 2 - tw // 2, y + h // 2 + th // 2)
            cv2.putText(imagem_cp, texto, pos_texto, fonte, 0.6, (0, 0, 255), 2)

        nome_saida = f"./data/result/saida_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.jpg"
        cv2.imwrite(nome_saida, imagem_cp)
        print(f"Imagem salva como: {nome_saida}")

        cv2.imshow("Quadrados Detectados", imagem_cp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()