import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from yt_dlp import YoutubeDL
from urllib.parse import urlparse

def is_url_valido(link):
    try:
        resultado = urlparse(link)
        return all([resultado.scheme, resultado.netloc])
    except:
        return False

def progresso(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        baixado = d.get('downloaded_bytes', 0)
        if total:
            percent = int(baixado * 100 / total)
            progress["value"] = percent
            status_label.config(text=f"Baixando... {percent}%")
            root.update_idletasks()
    elif d['status'] == 'finished':
        progress["value"] = 100
        status_label.config(text="Download finalizado!")

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
            'progress_hooks': [progresso],  # <- hook do progresso
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36',
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
root.geometry("550x230")

label = tk.Label(root, text="Insira o link do vídeo (YouTube, TikTok, Instagram, etc):")
label.pack(pady=10)

url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=10)

# Barra de progresso
progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress.pack(pady=5)

# Status do download
status_label = tk.Label(root, text="Aguardando...")
status_label.pack(pady=5)

root.mainloop()
