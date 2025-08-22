# file_manager.py
import os
import re


def sanitize_filename(filename: str) -> str:
    """
    Remove caracteres inválidos do nome do arquivo para evitar erros no sistema de arquivos.
    
    Args:
        filename (str): Nome original do arquivo.
        
    Returns:
        str: Nome do arquivo limpo e seguro para salvar.
    """
    # Remove caracteres não permitidos em sistemas operacionais
    return re.sub(r'[\\/*?:"<>|]', "_", filename)


def ensure_directory(path: str) -> None:
    """
    Garante que o diretório exista. Se não existir, ele é criado.
    
    Args:
        path (str): Caminho do diretório a ser verificado/criado.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def build_file_path(directory: str, filename: str, extension: str = ".mp4") -> str:
    """
    Cria o caminho completo do arquivo, já sanitizando o nome.
    
    Args:
        directory (str): Diretório onde o arquivo será salvo.
        filename (str): Nome base do arquivo.
        extension (str, opcional): Extensão do arquivo. Padrão: ".mp4".
    
    Returns:
        str: Caminho completo do arquivo.
    """
    ensure_directory(directory)
    safe_name = sanitize_filename(filename)
    return os.path.join(directory, safe_name + extension)
