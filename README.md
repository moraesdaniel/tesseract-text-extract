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

Para obter nossa imagem personalizada, basta utilizarmos o comando `docker build -t text-extract:latest .` (sim o ponto faz parte do comando), de dentro da pasta do projeto.
Substitua text-extract:latest, pelo nome e a tag que desejar. Só não esqueça de alterar depois o docker-compose.yaml também.

## Container
Está no projeto também um arquivo *docker-compose.yaml*, que nos ajudará a subir o container.
Esse container foi construído para ser usado em ambientes de desenvolvimento.
Nele usamos o comando sleep para manter o container em pé e podermos conectar nele para realizar nossos testes.
Compartilhamos também a pasta `src` do nosso host com a `/var/www` do container pelo mesmo motivo, podermos fazer alterações locais e testá-las de imediato dentro do container.
Para subir o container, basta utilizar o bom e velho `docker-compose up -d`.

## Código fonte
O código fonte é muito simples.
No início tem um comando bônus que vai nos mostrar as linguagens disponíveis na versão da biblioteca que instalamos.</br>
Primeiro utilizei o opencv para ler a imagem (`cv2.imread`).
Depois bastou submeter a imagem ao pytesseract (`pytesseract.image_to_string`), passando o parâmetro `lang='por'` para que a leitura reconheça caracteres da língua portuguesa, e exibir o resultado.

Com o resultado da leitura em mãos, podemos realizar várias tarefas, procurar termos com regex é uma delas. Agora basta você dar o destino que quiser para essas informações.