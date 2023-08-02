from tkinter import *
from tkinter import ttk


#Cores
Preto = "#000000" 
Laranja = "#F69906"
cinza_escuro = "#313131" 
cinza_claro = "#9F9F9F"
branco = "#fff"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x258")
janela.config(bg=Preto)

#Display resultado
frame_tela = Frame(janela, width=235, height=50, bg=Preto)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=Preto)
frame_corpo.grid(row=1, column=0)

#Labels

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, fg= branco, padx=7, relief=FLAT,anchor="e", justify=RIGHT, font='Montserat 18', bg=Preto)
app_label.place(x=0, y=0)

#Variável todos valores

todos_valores = ''

# Função

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)


#Passando o valor para a tela
    valor_texto.set(todos_valores)

#Função que calcula

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(resultado)

# Função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#Botões

b_ac = Button(frame_corpo, command = limpar_tela, text="AC", width=7, height=2, bg= cinza_claro, font='Montserat 9', relief=RAISED, overrelief=RIDGE)
b_ac.place(x=0, y=0)

b_mm = Button(frame_corpo, text="+/-", width=7, height=2, bg= cinza_claro, font='Montserat 9', relief=RAISED, overrelief=RIDGE)
b_mm.place(x=60, y=0)

b_porc = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=7, height=2, bg= cinza_claro, font='Montserat 9', relief=RAISED, overrelief=RIDGE)
b_porc.place(x=120, y=0)

b_divi = Button(frame_corpo, command = lambda: entrar_valores('/'),text="÷", width=7, height=2, bg= Laranja, fg=branco, font='Montserat 9', relief=RAISED, overrelief=RIDGE)
b_divi.place(x=180, y=0)

b_7 = Button(frame_corpo, command = lambda: entrar_valores('7'),text="7", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_7.place(x=0, y=42)

b_8 = Button(frame_corpo, command = lambda: entrar_valores('8'),text="8", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_8.place(x=60, y=42)

b_9 = Button(frame_corpo, command = lambda: entrar_valores('9'),text="9", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_9.place(x=120, y=42)

b_x = Button(frame_corpo, command = lambda: entrar_valores('*'),text="X", width=7, height=2, bg= Laranja, fg=branco, font='Montserat 9', relief=RAISED, overrelief=RIDGE)
b_x.place(x=180, y=42)

b_4 = Button(frame_corpo, command = lambda: entrar_valores('4'),text="4", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_4.place(x=0, y=84)

b_5 = Button(frame_corpo, command = lambda: entrar_valores('5'),text="5", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_5.place(x=60, y=84)

b_6 = Button(frame_corpo, command = lambda: entrar_valores('6'),text="6", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_6.place(x=120, y=84)

b_sub = Button(frame_corpo, command = lambda: entrar_valores('-'),text="-", width=7, height=2, bg= Laranja, fg=branco, font='Montserat 9', relief=RAISED, overrelief=RIDGE)
b_sub.place(x=180, y=84)

b_1 = Button(frame_corpo, command = lambda: entrar_valores('1'),text="1", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_1.place(x=0, y=126)

b_2 = Button(frame_corpo, command = lambda: entrar_valores('2'),text="2", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_2.place(x=60, y=126)

b_3 = Button(frame_corpo, command = lambda: entrar_valores('3'),text="3", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_3.place(x=120, y=126)

b_soma = Button(frame_corpo, command = lambda: entrar_valores('+'),text="+", width=7, height=2, bg= Laranja, fg=branco, font='Montserat 9', relief=RAISED, overrelief=RIDGE)
b_soma.place(x=180, y=126)

b_0 = Button(frame_corpo, command = lambda: entrar_valores('0'),text="0", width=16, height=2, bg= cinza_escuro, fg=branco, font='Montserat 9', relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=168)

b_comma = Button(frame_corpo, command = lambda: entrar_valores(','),text=",", width=7, height=2, bg= cinza_escuro, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_comma.place(x=120, y=168)

b_igual = Button(frame_corpo, command = calcular,text="=", width=7, height=2, bg= Laranja, font='Montserat 9', relief=RAISED, overrelief=RIDGE, fg=branco)
b_igual.place(x=180, y=168)


janela.mainloop()