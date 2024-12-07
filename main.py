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

frameBaixo = Frame(janela, width=1043, height=360, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

app_img = Image.open('moneylg.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text="Controle financeiro", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# função de porcentagem
def porcentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita gasta ", height=1, anchor=NW, font=("Verdana 12 "), bg=co1, fg=co4)
    l_nome.place(x=7, y=5)

    # definindo o estilo da ProgressBar
    style = ttk.Style()
    style.configure("TProgressbar",
                    thickness=20,  # espessura da barra
                    troughcolor=co1,
                    background=co2)

    # barra de progresso
    bar = Progressbar(frameMeio, length=180, style="TProgressbar")
    bar.place(x=10, y=35)

    # definindo valor da progressbar
    bar['value'] = 50
    valor = 50

    l_porcentagem = Label(frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=("Verdana 12 "), bg=co1, fg=co4)
    l_porcentagem.place(x=200, y=35)

# função para gráfico de barras
def grafico_bar():
    lista_categorias = ["Renda", "Despesas", "Saldo"]
    lista_valores = [300, 2000, 6236]

    # criando a figura do gráfico
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    ax.autoscale(enable=True, axis='both', tight=None)

    # plotando as barras
    ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)

    # adicionando rótulos nas barras
    c = 0
    for i in ax.patches:
        ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 50,
                str("{:,.0f}".format(lista_valores[c])), fontsize=12, fontstyle='italic', verticalalignment='bottom', color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias, fontsize=16)

    # ajustando o estilo do gráfico
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    # integrando o gráfico na interface Tkinter
    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)

# função resumo
def resumo():
    valor=[1200, 600, 3200]

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg="#545454")
    l_linha.place(x=309, y= 52)
    l_sumario = Label(frameMeio,text = "Renda Mensal".upper(), anchor=NW, font=("Verdana 12"), bg= co1, fg= "#83a9e6")
    l_sumario.place(x= 309, y=35)
    l_sumario= Label(frameMeio, text="R${:,.2f}".format(valor[0]), anchor=NW, font=("Arial 17 "),  bg= co1, fg="#545454")
    l_sumario.place(x=309, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg="#545454")
    l_linha.place(x=309, y= 132)
    l_sumario = Label(frameMeio,text = "Despesa  Mensal".upper(), anchor=NW, font=("Verdana 12"), bg= co1, fg= "#83a9e6")
    l_sumario.place(x= 309, y=115)
    l_sumario= Label(frameMeio, text="R${:,.2f}".format(valor[1]), anchor=NW, font=("Arial 17 "),  bg= co1, fg="#545454")
    l_sumario.place(x=309, y=150)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg="#545454")
    l_linha.place(x=309, y= 207)
    l_sumario = Label(frameMeio,text = "Saldo da Caixa".upper(), anchor=NW, font=("Verdana 12"), bg= co1, fg= "#83a9e6")
    l_sumario.place(x= 309, y=190)
    l_sumario= Label(frameMeio, text="R${:,.2f}".format(valor[2]), anchor=NW, font=("Arial 17 "),  bg= co1, fg="#545454")
    l_sumario.place(x=309, y=220)

# frame para o gráfico de pizza
frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_pie.place(x=415, y=5)

# função gráfico pie
def grafico_pie():
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345, 225, 534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']
    
    # Definir cores personalizadas para as fatias
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    # Explode as fatias um pouco, para destacar as partes do gráfico (ajustar se necessário)
    explode = [0.05] * len(lista_categorias)

    # Criando o gráfico de pizza com o formato de círculo completo
    ax.pie(lista_valores, explode=explode, autopct='%1.1f%%', colors=colors, shadow=True, startangle=45)

    # Título do gráfico
    ax.set_title("Resumo Financeiro", fontsize=14, fontweight="bold")

    # Legenda ajustada para ir para a direita
    ax.legend(lista_categorias, loc="center left", fontsize=12, bbox_to_anchor=(0.9, 0.5))

    # Removendo espaços em branco ao redor do gráfico
    figura.tight_layout(pad=0)  # Remove o padding extra
    
    figura.subplots_adjust(left=0.1)  # Ajuste o valor 'left' para mover o gráfico para a direita
    
    # Removendo espaços em branco ao redor do gráfico

    # Integra o gráfico na interface
    canva = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva.get_tk_widget().pack(fill=BOTH, expand=True)
    canva.draw()

# chamar as funções


## criando frame abaixo do medio 
frame_renda=Frame(frameBaixo, width=300, height= 250, bg=co1)
frame_renda.grid(row=0,column=0)


frame_operacoes=Frame(frameBaixo, width=220, height= 250, bg=co1)
frame_operacoes.grid(row=0,column=1,padx= 5)

frame_configuracao=Frame(frameBaixo, width=220, height= 250, bg=co1)
frame_configuracao.grid(row=0,column=2,padx= 5)

### tabela renda mensal 
app_tabela=Label(frameMeio, text="Tabelas Receitas e Despesas",anchor= NW, font=("Verdana 12"),bg=co1, fg=co4)
app_tabela.place(x=5, y=309)

def mostrar_renda():

   
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
   
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


grafico_bar()
porcentagem()
mostrar_renda()
resumo()
grafico_pie()
janela.mainloop()
