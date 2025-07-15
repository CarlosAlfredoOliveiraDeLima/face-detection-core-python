# Face Detection Core Python

Uma API Flask para detecção de rostos em imagens usando OpenCV, projetada como um microserviço eficiente que processa imagens e retorna anotações visuais dos rostos detectados.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.1-green.svg)
![OpenCV](https://img.shields.io/badge/opencv-4.12.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Descrição

Este projeto oferece uma API REST simples e eficiente para detectar rostos em imagens usando algoritmos de visão computacional. A aplicação recebe imagens em formato base64, processa-as usando classificadores Haar Cascade do OpenCV e retorna as imagens com retângulos desenhados ao redor dos rostos detectados.

## Funcionalidades

-  Detecção automática de rostos em imagens
-  Processamento de imagens em formato base64
-  Retorno de imagens anotadas com retângulos verdes
-  Contagem do número de rostos detectados
-  API REST simples e intuitiva
-  Tratamento de erros robusto

##  Tecnologias Utilizadas

- **[Python 3.8+](https://python.org/)** - Linguagem principal
- **[Flask 3.1.1](https://flask.palletsprojects.com/)** - Framework web
- **[OpenCV 4.12.0](https://opencv.org/)** - Biblioteca de visão computacional
- **[NumPy 2.2.6](https://numpy.org/)** - Processamento de arrays
- **Haar Cascade Classifier** - Algoritmo de detecção facial

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/face-detection-core-python.git
   cd face-detection-core-python
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements
   ```

4. **Execute a aplicação**
   ```bash
   python app/main.py
   ```

A API estará disponível em `http://localhost:5000`

## Estrutura do Projeto

```
face-detection-core-python/
├── app/
│   ├── ml_utils/
│   │   └── face_detection.py    # Lógica de detecção facial
│   └── main.py                  # Aplicação Flask principal
├── .venv/                       # Ambiente virtual
├── requirements                 # Dependências do projeto
├── output.jpg                   # Imagem de exemplo/teste
└── README.md                    # Este arquivo
```

## Como Usar

### Endpoint Principal

**POST** `/process-image`

### Requisição

```json
{
  "image": "base64_encoded_image_data"
}
```

### Resposta de Sucesso

```json
{
  "success": true,
  "processed_image": "base64_encoded_processed_image",
  "format": "jpeg",
  "faces_count": 2
}
```

### Exemplo com cURL

```bash
curl -X POST http://localhost:5000/process-image \
  -H "Content-Type: application/json" \
  -d '{
    "image": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChAG..."
  }'
```

### Exemplo com Python

```python
import requests
import base64

# Carregar e codificar imagem
with open('sua_imagem.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

# Fazer requisição
response = requests.post('http://localhost:5000/process-image', json={
    'image': image_data
})

result = response.json()
print(f"Rostos detectados: {result['faces_count']}")
```

## Configuração de Detecção

O algoritmo utiliza os seguintes parâmetros otimizados:

- **scaleFactor**: 1.01 - Redução da imagem a cada escala
- **minNeighbors**: 10 - Número mínimo de vizinhos para confirmar detecção
- **minSize**: (100, 100) - Tamanho mínimo do rosto em pixels
- **Cor do retângulo**: Verde (0, 255, 0)
- **Espessura**: 2 pixels

## Testando a API

### Com Postman

1. Configure o método como **POST**
2. URL: `http://localhost:5000/process-image`
3. Header: `Content-Type: application/json`
4. Body: JSON com imagem em base64

### Com arquivo de teste

O projeto inclui um arquivo `input.jpg` que pode ser usado para testes.
No diretório raíz também há um arquivo `output.jpg` com o resultado esperado.

## Tratamento de Erros

A API retorna os seguintes códigos de erro:

- **400**: Dados inválidos ou imagem não pôde ser decodificada
- **500**: Erro interno do servidor

Exemplo de resposta de erro:

```json
{
  "error": "Failed to decode image"
}
```

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

- **Carlos Alfredo Oliveira de Lima** - [GitHub](https://github.com/CarlosAlfredoOliveiraDeLima)

## Agradecimentos

- **OpenCV Community** - Pela excelente biblioteca de visão computacional
- **Flask Team** - Pelo framework web minimalista e eficiente
- **Haar Cascade** - Pelo algoritmo de detecção facial robusto

---

 **Gostou do projeto? Deixe uma estrela!** 