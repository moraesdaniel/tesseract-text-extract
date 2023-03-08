# Tesseract TextExtract
Esse projeto utiliza a biblioteca Tesseract com Python para extrair textos de imagens.

## Ambiente
Ao escolher a imagem do Python, tentei escolher a mais leve que atendesse aos requisitos.
Tentei levantar sobre a imagem `python:3.10-slim` e `python:3.10-alpine`, porém, em ambas, tive dificuldades para compilar e instalar a biblioteca `numpy`.
Nas imagens `slim-buster`, `buster` e `bullseye`, funcionou perfeitamente. Contudo, escolhi a `slim-buster` devido ao critério que citei anteriormente, por ser mais leve.