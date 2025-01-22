import sqlite3 as lite

con = lite.connect('dados.db')


def inserir_categoria(i):
   with con:
      cur = con.cursor()
      query = "INSERT INTO Categoria (nome) VALUES(?)"
      cur.execute(query, (i,))
      print(f"Categoria '{i}' inserida com sucesso!")


def inserir_receita(i):
   with con:
      cur = con.cursor()
      query = "INSERT INTO Receitas (categoria, adicionando_em, valor) VALUES(?, ?, ?)"
      cur.execute(query, i)


def inserir_gasto(i):
   with con:
      cur = con.cursor()
      query = "INSERT INTO Gastos (categoria, retirando_em, valor) VALUES(?, ?, ?)"
      cur.execute(query, i)


def deletar_receita(i):
   with con:
      cur = con.cursor()
      query = "DELETE FROM Receitas WHERE id=?"
      cur.execute(query, (i,)) 


def deletar_gasto(i):
   with con:
      cur = con.cursor()
      query = "DELETE FROM Gastos WHERE id=?"
      cur.execute(query, (i,)) 


def ver_categoria():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linhas = cur.fetchall()
        for l in linhas:
            lista_itens.append(l)
    return lista_itens


def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linhas = cur.fetchall()
        for l in linhas:
            lista_itens.append(l)
    return lista_itens


def ver_receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linhas = cur.fetchall()
        for l in linhas:
            lista_itens.append(l)
    return lista_itens
def tabela():
    gastos= ver_gastos()
    receitas= ver_receitas()
    
    tabela_lista=[]

    for i in gastos:
        tabela_lista.append(i)
    for i in receitas:
        tabela_lista.append(i)
    return tabela_lista

def bar_valores():
    total_receitas = 0
    total_gastos = 0

   
    with con:
        cur = con.cursor()
        cur.execute("SELECT valor FROM Receitas")
        receitas = cur.fetchall()
        for receita in receitas:
            total_receitas += receita[0]

   
    with con:
        cur = con.cursor()
        cur.execute("SELECT valor FROM Gastos")
        gastos = cur.fetchall()
        for gasto in gastos:
            total_gastos += gasto[0]

    return total_receitas, total_gastos


