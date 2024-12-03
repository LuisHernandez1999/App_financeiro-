from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure
# definição das cores
co0 = "#2eb2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

colors = ["#5588bb", "#66bbbb", "#99bb55", "#444466", "#bb5555"]

# criando a janela
janela = Tk()
janela.title("Controle Financeiro")
janela.geometry("900x650")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

# configuração do estilo
style = ttk.Style(janela)
style.theme_use("clam")

# divisão da tela
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


frameBaixo = Frame(janela, width=1043, height=360, bg=co1,relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)


app_img= Image.open('moneylg.png')
app_img=app_img.resize((45,45))
app_img= ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image= app_img, text = "Controle financeiro", width= 900, compound= LEFT, padx=5, relief=RAISED,anchor=NW, font=('Verdana 20 bold'), bg = co1, fg= co4,)
app_logo.place(x=0, y=0)


def porcentagem():
    l_nome = Label(frameMeio, text = "Porcentagem da Receita gasta ", height=1,anchor=NW, font=("Verdana 12 "), bg=co1,fg= co4 )
    l_nome.place(x=7, y=5)

style = ttk.Style()

# definindo o estilo da Progressbar
style.configure("TProgressbar",
                thickness=20,  # espessura da barra
                troughcolor=co1,  
                background=co2, 
                )

# barra de progresso
bar = Progressbar(frameMeio, length=180, style="TProgressbar")
bar.place(x= 10, y= 35)

# definindo valor da progressbar
bar['value'] = 50
valor = 50 

l_porcentagem = Label(frameMeio, text ="{:,.2f}%".format(valor),anchor=NW, font=("Verdana 12 "), bg=co1,fg= co4 )
l_porcentagem.place(x=200, y=35)


porcentagem()
# executando a janela
janela.mainloop()
