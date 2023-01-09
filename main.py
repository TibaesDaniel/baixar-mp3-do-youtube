from pytube import YouTube
from tkinter import *
import moviepy.editor as mp
import re
import os


janela = Tk()
janela.geometry('500x250')

def exeVideo():
    link = inpLinks.get()
    path = "Aguardando"
    yt = YouTube(link)

    print("Baixando...")
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print("Download completo")

    print("Convertendo arquivo...")
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print('Sucesso!')


janela.title("Baixar Musicas da Sil")
titulo = Label(janela, text="Utilize com resposabilidade, nao vai baixar musicas dos anos 70, é muito viciante!!!")
titulo.grid(row=1, column=0)

label1 = Label(janela, text="Link do Youtube")
label1.grid(row=2, column=0)
inpLinks = Entry(janela, width=70, font=("Arial 10"))
inpLinks.grid(row=4, column=0)

btn = Button(janela, width=20, height=2, text="Executar", command=exeVideo)
btn.grid(row=5, column=0)


janela.mainloop()