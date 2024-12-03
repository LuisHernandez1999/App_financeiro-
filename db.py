import sqlite3 as lite 

con= lite.connect('dados.db')


with con: 
    cur = con.cursor()
    cur.execute("CREATE TABLE  Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT ,nome TEXT)")


with con: 
    cur = con.cursor()
    cur.execute("CREATE TABLE  Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT , categoria TEXT, adicionando_em DATE,valor DECIMAL)")

with con: 
    cur = con.cursor()
    cur.execute("CREATE TABLE  Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT , categoria TEXT, retirando_em DATE,valor DECIMAL)")