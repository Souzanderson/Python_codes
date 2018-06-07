#App: calculadora em python
#versão: 1.0

from tkinter import*
from functools import partial

class Calculadora(object):
    def __init__(self,app):
        
        buts=('1','2','3','+','4','5','6','-','7','8','9','x','.','0','%','/','C','^','sqrt','=')

        #frame do visor
        self.frame1 = Frame(app)

        #frame dos botões
        self.frame2 = Frame(app)

        #empacotar as frames
        self.frame1.pack()
        self.frame2.pack()
        
        #visor
        self.form = Entry(self.frame1,width=42)
        self.form.pack()

        #botões
        for i in range(len(buts)):
            if i%4==0:
                subframe = Frame(self.frame2)
                subframe.pack()
            but = Button(subframe, text=buts[i],padx=18,pady=4, width=3, command=partial(self.Calc, buts[i]))
            but.pack(side= LEFT)

    def Calc(self, texto):
            global op
            global a
            global b

            if texto=='C':
                self.form.delete(0,END)
            elif texto=='+' or texto=='-' or texto=='x' or texto=='/':
                op=texto
                a=float(self.form.get())
                self.form.delete(0,END)
            elif texto=='=':
                b=float(self.form.get())
                self.form.delete(0,END)
                if op=='+':
                    c=str(a+b)
                if op=='-':
                    c=str(a-b)
                if op=='x':
                    c=str(a*b)
                if op=='/':
                    c=str(a/b)
                self.form.insert(END,c)
            else:
                self.form.insert(END, texto)
            
                         

#Criar tela
app = Tk()

#Título
app.title("Calculadora")

#Tamanho da tela
app.geometry("270x182")

#instancia a calculadora
Calculadora(app)

#inicia o programa
app.mainloop()
