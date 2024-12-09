import sqlite3 as lite

con = lite.connect('dados.db')

# Função para inserir categorias
def inserir_categoria(i):
   with con:
      cur = con.cursor()
      query = "INSERT INTO Categoria (nome) VALUES(?)"
      cur.execute(query, (i,))
      print(f"Categoria '{i}' inserida com sucesso!")

# Função para inserir receita
def inserir_receita(i):
   with con:
      cur = con.cursor()
      query = "INSERT INTO Receitas (categoria, adicionando_em, valor) VALUES(?, ?, ?)"
      cur.execute(query, i)

# Função para inserir gasto
def inserir_gasto(i):
   with con:
      cur = con.cursor()
      query = "INSERT INTO Gastos (categoria, retirando_em, valor) VALUES(?, ?, ?)"
      cur.execute(query, i)

# Função para deletar receita
def deletar_receita(i):
   with con:
      cur = con.cursor()
      query = "DELETE FROM Receitas WHERE id=?"
      cur.execute(query, (i,))  # Passando como tupla

# Função para deletar gasto
def deletar_gasto(i):
   with con:
      cur = con.cursor()
      query = "DELETE FROM Gastos WHERE id=?"
      cur.execute(query, (i,))  # Passando como tupla

# Função para ver categorias
def ver_categoria():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linhas = cur.fetchall()
        for l in linhas:
            lista_itens.append(l)
    return lista_itens

# Função para ver gastos
def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linhas = cur.fetchall()
        for l in linhas:
            lista_itens.append(l)
    return lista_itens

# Função para ver receitas
def ver_receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linhas = cur.fetchall()
        for l in linhas:
            lista_itens.append(l)
    return lista_itens

# Função para calcular o total de valores de receitas e gastos (bar_valores)
def bar_valores():
    total_receitas = 0
    total_gastos = 0

    # Somar os valores das receitas
    with con:
        cur = con.cursor()
        cur.execute("SELECT valor FROM Receitas")
        receitas = cur.fetchall()
        for receita in receitas:
            total_receitas += receita[0]

    # Somar os valores dos gastos
    with con:
        cur = con.cursor()
        cur.execute("SELECT valor FROM Gastos")
        gastos = cur.fetchall()
        for gasto in gastos:
            total_gastos += gasto[0]

    return total_receitas, total_gastos


