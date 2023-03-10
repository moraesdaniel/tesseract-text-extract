# Tesseract TextExtract
Esse projeto utiliza a biblioteca Tesseract com Python para extrair textos de imagens.

**Table of contents**</br>
[1.0 - Ambiente](#ambiente)</br>
&nbsp;&nbsp;&nbsp;&nbsp;[1.1 - Imagem do Container](#imagem-do-container)</br>
&nbsp;&nbsp;&nbsp;&nbsp;[1.2 - Bliblioteca libgl](#bliblioteca-libgl1)</br>
&nbsp;&nbsp;&nbsp;&nbsp;[1.3 - Biblioteca Tesseract OCR](#bliblioteca-tesseract-ocr)</br>
[2.0 - Container](#container)</br>
[3.0 - Código Fonte](#código-fonte)</br>
[4.0 - Fontes](#fontes)</br>

## Ambiente
### Imagem do Container
Ao escolher a imagem do Python, tentei escolher a mais leve que atendesse aos requisitos.
Tentei levantar sobre a imagem `python:3.10-slim` e `python:3.10-alpine`, porém, em ambas, tive dificuldades para compilar e instalar a biblioteca `numpy`.</br>
Nas imagens `slim-buster`, `buster` e `bullseye`, funcionou perfeitamente. Contudo, escolhi a `slim-buster` devido ao critério que citei anteriormente, por ser mais leve.
### Bliblioteca libgl1
Mesmo escolhendo a imagem slim-buster, ainda aconteciam erros ao compilar e instalar a `numpy`. Instalando a `libgl1`, esses erros foram sanados.
### Bliblioteca Tesseract OCR
Ao instalar a bliblioteca padrão, `tesseract-ocr`, não temos a versão português, o que fazia caracteres como **ç** não serem reconhecidos. Instalando a versão `tesseract-ocr-por`, ganhamos esse recurso a mais.

Daqui em diante é instalação padrão, atualizamos o aplicativo pip, copiamos o txt com a listagem de bibliotecas necessárias e as instalamos.

Para obter nossa imagem personalizada, basta utilizarmos o comando `docker build -t text-extract:latest .` (sim o ponto faz parte do comando), de dentro da pasta do projeto.
Substitua text-extract:latest, pelo nome e a tag que desejar. Só não esqueça de alterar depois o docker-compose.yaml também.

## Container
Está no projeto também um arquivo *docker-compose.yaml*, que nos ajudará a subir o container.</br>
Esse container foi construído para ser usado em ambientes de desenvolvimento.</br>
Nele usamos o comando sleep para manter o container em pé e podermos conectar nele para realizar nossos testes.</br>
Compartilhamos também a pasta `src` do nosso host com a `/var/www` do container pelo mesmo motivo, podermos fazer alterações locais e testá-las de imediato dentro do container.</br>
Para subir o container, basta utilizar o bom e velho `docker-compose up -d`.

## Código Fonte
O código fonte é muito simples.</br>
No início tem um comando bônus que vai nos mostrar as linguagens disponíveis na versão da biblioteca que instalamos.</br>
Primeiro utilizei o opencv para ler a imagem (`cv2.imread`).</br>
Depois bastou submeter a imagem ao pytesseract (`pytesseract.image_to_string`), passando o parâmetro `lang='por'` para que a leitura reconheça caracteres da língua portuguesa, e exibir o resultado.

Com o resultado da leitura em mãos, podemos realizar várias tarefas, procurar termos com regex é uma delas. Agora basta você dar o destino que quiser para essas informações.

## Fontes:
[Como transformar imagem em texto usando o OCR em Python com OpenCV, Tesseract reconhecendo caracteres](https://youtu.be/GMqFZ7f0dy4)</br>
[OCR com Tesseract e Python](https://youtu.be/MfKvjWrcdaY)</br>
[Erro ao compilar o numpy](https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo)</br>
[Como instalo um novo pacote de idiomas para o Tesseract](https://sobrelinux.info/questions/13937/how-do-i-install-a-new-language-pack-for-tesseract-on-16-04)</br>