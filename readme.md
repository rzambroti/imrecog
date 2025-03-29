# Gabarito Corretor

Este é um projeto Python em desenvolvimento com o objetivo de criar um software capaz de **identificar automaticamente as respostas marcadas por alunos em gabaritos físicos preenchidos à mão**.

O sistema utiliza técnicas de **processamento de imagem**, detecção de contornos e lógica de validação geométrica para localizar e interpretar os quadrados preenchidos no gabarito.

---

## 🧠 Objetivo do projeto

A ideia central é que, com uma simples foto ou digitalização (scan) de um gabarito, o sistema possa:

1. Detectar automaticamente os **quadrados preenchidos** pelo aluno.
2. Mapear, em um segundo momento, **a qual alternativa (coluna A, B, C, D)** o quadrado corresponde.
3. Comparar com um gabarito oficial e gerar um **relatório de acertos e erros**.

---

## 📄 Sobre o layout do gabarito

Para facilitar o reconhecimento, o modelo de gabarito utilizado possui:

- **QR Codes** ao lado de cada linha de questão, com o número da questão codificado (ainda não utilizados na versão atual).
- Uma **linha de cabeçalho** com quadrados preenchidos nas posições das colunas `A`, `B`, `C` e `D`.
- Uma **linha de rodapé** com os mesmos quadrados para reforçar o alinhamento das colunas.
- **Um quadrado marcador no fim de cada linha** de questão, utilizado como referência para saber onde termina cada linha.

---

## 🚧 Status atual do projeto

- ✅ Leitura e carregamento de imagem (PDF ou JPG, PNG, etc.)
- ✅ Detecção robusta dos quadrados preenchidos, evitando contornos duplicados.
- ✅ Visualização com marcação e numeração dos quadrados detectados.
- 🔜 Mapeamento das posições dos quadrados detectados em relação às colunas (A, B, C, D).
- 🔜 Leitura dos QR Codes para identificar as questões (em versões futuras).
- 🔜 Geração de relatórios comparando com gabarito oficial.

---

## 🧩 Tecnologias utilizadas

- Python 3.10+
- OpenCV
- Pillow
- NumPy
- pdf2image
- PyMuPDF (em versões futuras)

---

## 🤝 Contribuições

Contribuições são muito bem-vindas! Você pode ajudar com:

- Código (detecção, melhorias de OCR, performance)
- Sugestões de layout para os gabaritos
- Testes com diferentes modelos de escaneamento
- Documentação

Para contribuir, siga o fluxo padrão de fork, branch e pull request.  
Você também pode abrir uma [issue](https://github.com/rzambroti/imrecog/issues) com bugs, ideias ou dúvidas.

---

## 📁 Organização do código

# /imrecog/
# ├── main.py
# ├── data/
# │   ├── gabarito_preenchido1.jpg
# ├── core/
# │   ├── image_loader.py
# │   ├── square_detector.py
# │   ├── visualizer.py
# ├── utils/
# │   └── geometry.py