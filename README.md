# Tesseract TextExtract
Esse projeto utiliza a biblioteca Tesseract com Python para extrair textos de imagens.

## Ambiente
### Imagem do container
Ao escolher a imagem do Python, tentei escolher a mais leve que atendesse aos requisitos.
Tentei levantar sobre a imagem `python:3.10-slim` e `python:3.10-alpine`, porém, em ambas, tive dificuldades para compilar e instalar a biblioteca `numpy`.
Nas imagens `slim-buster`, `buster` e `bullseye`, funcionou perfeitamente. Contudo, escolhi a `slim-buster` devido ao critério que citei anteriormente, por ser mais leve.
### Bliblioteca libgl1
Mesmo escolhendo a imagem slim-buster, ainda aconteciam erros ao compilar e instalar a `numpy`. Instalando a `libgl1`, esses erros foram sanados.
### Bliblioteca Tesseract OCR
Ao instalar a bliblioteca padrão, `tesseract-ocr`, não temos a versão português, o que fazia caracteres como **ç** não serem reconhecidos. Instalando a versão `tesseract-ocr-por`, ganhamos esse recurso a mais.

Daqui em diante é instalação padrão, atualizamos o aplicativo pip, copiamos o txt com a listagem de bibliotecas necessárias e as instalamos.