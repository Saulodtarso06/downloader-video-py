# 📥 Downloader-Video-Py

Um aplicativo simples em **Python** para baixar vídeos do **YouTube** utilizando a biblioteca [Pytube](https://pytube.io/) e interface gráfica com **Tkinter**.

---

## 🚀 Funcionalidades

- Baixar vídeos do YouTube em formato **.mp4**
- Escolher diretório de salvamento
- Interface gráfica simples e intuitiva com Tkinter
- Exibição de mensagens de status (início, progresso e conclusão do download)

---

## 🛠️ Tecnologias utilizadas

- **Python 3.x**
- **Tkinter** (interface gráfica)
- **Pytube** (download de vídeos do YouTube)
- **OS / Sys** (manipulação de diretórios e arquivos)

---

## 📂 Estrutura do Projeto

downloader-video-py/
│-- main.py # Código principal do programa
│-- README.md # Documentação
│-- requirements.txt # Dependências do projeto

---

## ⚙️ Instalação

1. Clone este repositório:

```
git clone https://github.com/seu-usuario/downloader-video-py.git
```
---
 2. Acesse a pasta do projeto:

```
cd downloader-video-py
```
---
3. Crie um ambiente virtual (opcional, mas recomendado):

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
---
4. Instale as dependências:

```
pip install -r requirements.txt
```

▶️ Como usar

1. Execute o programa:

```
python main.py
```
2. Cole a URL do vídeo do YouTube na caixa de texto.

3. Escolha o diretório para salvar o arquivo.
---

## 📸 Captura de Tela.

(adicione aqui uma imagem da interface do programa, se desejar)

---

## Melhorias a serem implementadas:

Suporte para download de playlists

Opção de extrair apenas o áudio (MP3)

Barra de progresso em tempo real

Suporte a múltiplos downloads simultâneos