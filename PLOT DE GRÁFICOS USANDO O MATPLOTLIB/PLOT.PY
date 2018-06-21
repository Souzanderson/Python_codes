from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *
from tkinter import messagebox

#define a variável
x=symbols('x')


#função que plota o gráfico
def plotar():
    try:
        #convertendo o texto da entrada para expressão
        f=parse_expr(e.get())
        #comando de plot
        plot(f)
    except:
        messagebox.showerror("Erro!","Expressão indefinida!")

#criação da janela
app = Tk()
app.title('Gráficos')
l=Label(app,text="Expressão:")
l.pack(side=LEFT)
e=Entry(app)
e.pack(side=LEFT)
b=Button(app, text="plotar",command=plotar)
b.pack(side=LEFT)



app.mainloop()
