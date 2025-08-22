# test_utils.py
import os
import pytest
from utils import validar_url, gerar_nome_arquivo, checar_diretorio

def test_validar_url_valida():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert validar_url(url) is True

def test_validar_url_invalida():
    url = "htp:/youtube.com/abc"
    assert validar_url(url) is False

def test_gerar_nome_arquivo_com_titulo():
    titulo = "Meu Vídeo de Teste"
    filename = gerar_nome_arquivo(titulo)
    assert filename.startswith("Meu_Vídeo_de_Teste")
    assert filename.endswith(".mp4")

def test_gerar_nome_arquivo_sem_titulo():
    filename = gerar_nome_arquivo("")
    assert filename.startswith("video_")
    assert filename.endswith(".mp4")

def test_checar_diretorio_existente(tmp_path):
    path = tmp_path / "videos"
    os.makedirs(path)
    assert checar_diretorio(str(path)) is True

def test_checar_diretorio_inexistente(tmp_path):
    path = tmp_path / "inexistente"
    assert checar_diretorio(str(path)) is False
