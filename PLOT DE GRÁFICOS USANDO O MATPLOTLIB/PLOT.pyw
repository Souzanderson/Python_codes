from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

#define as variáveis
x=symbols('x')
global e,f
e=[]
f=[]


#função que plota o gráfico
def plotar():
   # try:
        #convertendo o texto da entrada para expressão
        for i in range(len(e)):
            f.append(parse_expr(e[i].get()))
            plt.plot(x,f[i])
        plt.show()
   # except:
       # messagebox.showerror("Erro!","Expressão indefinida!")

def adicionar():
    subframe=Frame(app)
    subframe.pack()
    e.append(Entry(subframe))
    e[len(e)-1].pack(side=LEFT)
    b2=Button(subframe, text="+",command=adicionar)
    b2.pack(side=LEFT)
    
#criação da janela
app = Tk()
app.title('Gráficos')
l=Label(app,text="Expressão:")
l.pack()

adicionar()

b=Button(app, text="plotar", command=plotar)
b.pack(side=LEFT)
#execução do programa
app.mainloop()
