import sqlite3 as lite 

con = lite.connect('dados.db')

def inserir_categoria(i):
   with con:
    cur=con.cursor()
    query= "INSERT INTO Categoria (nome) VALUES(?)"
    cur.execute(query, (i,))
    print(f"Categoria '{i}' inserida com sucesso!")




def inserir_receita(i):
   with con:
    cur=con.cursor()
    query= "INSERT INTO Receita (categoria,adicionando_em,valor) VALUES(?,?,?)"
    cur.execute(query,i)



##### gastos
def inserir_receita(i):
   with con:
    cur=con.cursor()
    query= "INSERT INTO Gastos (categoria,retirando_em,valor) VALUES(?,?,?)"
    cur.execute(query,i)


##### funcoes pra deletar 
def deletar_receitas (i):
  with con: 
   cur=con.cursor()
   query="DELETE FROM Receitas WHERE id=?"
   cur.execute(query, i)

def deletar_gastos (i):
  with con: 
   cur=con.cursor()
   query="DELETE FROM Gastos WHERE id=?"
   cur.execute(query, i)


# funcoes pra ver dados 

#categoria 
def ver_categoria():
 lista_itens= []

 with con: 
   cur=con.cursor()
   cur.execute("SELECT * FROM Categoria")
   linha= cur.fetchall()
   for l in linha:
     lista_itens.append(l)

   return lista_itens
 
print(ver_categoria())

inserir_categoria("Alimentação")
# gastos 
def ver_gastos():
  lista_itens=[]
  with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Gastos")
    linha= cur.fetchall()
    for  l in linha:
      lista_itens.append(l)
   
    return lista_itens

