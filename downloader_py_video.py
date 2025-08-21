import tkinter as tk
from tkinter import messagebox, filedialog
from yt_dlp import YoutubeDL
from urllib.parse import urlparse

def is_url_valido(link):
    try:
        resultado = urlparse(link)
        return all([resultado.scheme, resultado.netloc])
    except:
        return False

def download_video():
    link = url_entry.get().strip()

    if not link:
        messagebox.showwarning("Erro", "Por favor, insira um link de vídeo.")
        return

    if not is_url_valido(link):
        messagebox.showerror("Erro", "Link inválido. Verifique se está completo (https://...)")
        return

    pasta_destino = filedialog.askdirectory(title="Escolha a pasta para salvar o vídeo")
    if not pasta_destino:
        return

    try:
        ydl_opts = {
            'outtmpl': f'{pasta_destino}/%(title).80s.%(ext)s',
            'format': 'best',
            'merge_output_format': 'mp4',
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36',
            'verbose': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        messagebox.showinfo("Sucesso", "Download concluído com sucesso.")
    except Exception as e:
        erro = str(e)
        if "403" in erro:
            mensagem = "Acesso negado. O vídeo pode ser privado ou restrito."
        elif "404" in erro:
            mensagem = "Vídeo não encontrado. Verifique o link."
        else:
            mensagem = f"Falha no download: {erro}"
        messagebox.showerror("Erro", mensagem)

# Interface Tkinter
root = tk.Tk()
root.title("Multi Video Downloader")
root.geometry("500x180")

label = tk.Label(root, text="Insira o link do vídeo (YouTube, TikTok, Instagram, etc):")
label.pack(pady=10)

url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=20)

root.mainloop()
