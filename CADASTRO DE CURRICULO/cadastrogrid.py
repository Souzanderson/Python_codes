from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3

class Cadastro(object):
    def __init__(self,app):

        campos = """Nome,Estado Civil,Idade,Endereço,Cidade/Estado,Telefone,Email,Habilitação"""
        campos=campos.split(",")
        buts = ["Salvar","Buscar","Deletar","Limpar"]
        global e
        e=[]
        
        for i in range(len(campos)):
            Label(app, text=campos[i]).grid(row=i, sticky=W,ipady=7,ipadx=25)
            e.append(Entry(app,width=50))
            e[i].grid(row=i, column=1, columnspan=len(buts))
   
        for i in range(len(buts)):
            Button(app, text=buts[i], padx=20, command=partial(self.cad_pessoa, buts[i])).grid(row=len(campos),column=i)

    def cad_pessoa(self,comando):
        if comando=="Salvar":
            try:
                
                nome=e[0].get()
                ec=e[1].get()
                idade=e[2].get()
                ender=e[3].get()
                city=e[4].get()
                fone=e[5].get()
                email=e[6].get()
                hab=e[7].get()

                #salvando no banco
                self.salva_banco(nome,ec,idade,ender,city,fone,email,hab)
                
                for i in range(8):
                    e[i].delete(0,END)
            except:
                messagebox.showinfo("Erro","Campo incorreto!")

        if comando=="Buscar":
            self.buscar_todos()

    def salva_banco(self, nome,ec,idade,ender,city,fone,email,hab):
        conn = sqlite3.connect('curriculo.db')
        cursor = conn.cursor()
                
        cursor.execute("""
        INSERT INTO pessoa (nome, ec, idade, ender, city, fone, email, hab)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (nome,ec,idade,ender,city,fone,email,hab))

        conn.commit()
        messagebox.showinfo("Salvo","Salvo com sucesso!")
        conn.close()

    def buscar_todos(self):
        conn = sqlite3.connect('curriculo.db')
        cursor = conn.cursor()
        
        sql = 'SELECT * FROM pessoa ORDER BY nome'
        r = cursor.execute(sql)
        lista = r.fetchall()
        
        for c in lista:
            print('\n-----------------------\nid:{:3d}\nNome:{:23s}\nEst.Civil: {:12s}\nIdade: {:s}\nEndereco: {:>25s}\nCidade: {:s}\nFone: {:15s}\nEmail: {:s}\nHabilitacao: {:s}'.format(
                c[0], c[1], c[2],
                c[3], c[4], c[5],
                c[6], c[7], c[8]))
        conn.close()
                
                   
    
#criar app
app = Tk()
app.title("Cadastro")
app.geometry("490x340")

#chamar app
Cadastro(app)

app.mainloop()
        

        
