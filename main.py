from core.image_loader import ImageLoader
from core.square_detector import SquareDetector
from core.visualizer import Visualizer


def main():
    caminho = "data/gabarito_preenchido1.jpg"

    # Carregar imagem
    imagem = ImageLoader().carregar(caminho)

    # Detectar quadrados
    detector = SquareDetector(gray_thresh=130, ink_thresh=145)
    quadrados = detector.detectar(imagem)

    # Visualizar resultado
    Visualizer().exibir(imagem, quadrados)


if __name__ == "__main__":
    main()