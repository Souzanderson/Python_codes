from tkinter import *

class Cadastro(object):
    def __init__(self,app):

        campos = """Nome,Estado Civil,Idade,Endereço,Cidade/Estado,Telefone,Email,Habilitação"""
        campos=campos.split(",")
        buts = ["Salvar","Buscar","Deletar"]
        
        #frame da tela de cadastro
        self.framecad=Frame(app)
        self.framecad.pack()        

        #frame dos botões
        self.framebot=Frame(app)
        self.framebot.pack()

        #campos
        self.label=[]
        self.form=[]
        for i in range(len(campos)):
            subframe=Frame(self.framecad,pady=7)
            subframe.pack()
            self.label.append(Label(subframe,text=campos[i]+": "))
            self.label[i].pack(side=LEFT)
        
            self.form.append(Entry(subframe,width=70))
            self.form[i].pack(side=LEFT)

        #botões
        for i in range(len(buts)):
            subframe=Frame(self.framebot,padx=12,pady=14)
            subframe.pack(side=LEFT)
            self.salvar=Button(subframe, text=buts[i],padx=25)
            self.salvar.pack()

        self.form[0].insert(END,"aqui")

#criar app
app = Tk()
app.title("Cadastro")
app.geometry("590x340")

#chamar app
Cadastro(app)

app.mainloop()
        

        
