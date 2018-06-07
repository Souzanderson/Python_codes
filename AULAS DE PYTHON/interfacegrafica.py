from tkinter import *

#funções

def Calcular():
    result['text'] = form.get() #move o texto da form para o Label Result
    result['fg']='red' #muda a cor do texto do Label Result


#cria a tela
app=Tk()

#define o tamanho da tela
app.geometry("400x300")

#titulo do programa
app.title("Calculadora")

#icone da tela
app.wm_iconbitmap('img/calc.ico')

#__________________conteudo do programa__________________

#texto (text = texto do label, bg= fundo, fg = cor do texto)
titulo=Label(app, text="Calculadora:", bg="grey", fg="black")
titulo.pack()

#entrada de texto
form=Entry(app)
form.pack()

#botão de calcular
button= Button(app, text="Calcular", pady=4, command=Calcular)
button.pack()

#texto de resultado
result=Label(app, text="resultado", pady=14)
result.pack()

#________________________________________________________

#inicia o programa
app.mainloop()
