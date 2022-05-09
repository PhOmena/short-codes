from tkinter import Tk
from tkinter import *
from tkinter import ttk
from datetime import date
import os
import pyautogui
import openpyxl

# Função acionada pelo botão
def compra():
    # Pega valores colocados nos inputs
    v_item = str(tb_item1.get())
    v_quant = tb_quantity1.get()

    # Se os inputs não forem vazios
    if tb_item1.get() and tb_quantity1.get() != "":
        # Abre o arquivo
        book = openpyxl.load_workbook("feira.xlsx")
        # Seleciona a planilha desejada
        itens_page = book['Compra']
        # Adiciona (OBS: Ele sempre adiciona na primeira linha vazia,
        # Portando, não precisa loopar.
        itens_page.append(["Maçã", 2, {dateBRL}])
        # Salva a planilha
        book.save("feira.xlsx")
        # Apaga os valores colocados nos inputs
        tb_item1.delete(0, END)
        tb_quantity1.delete(0, END)
        # Foca em um input
        tb_item1.focus()
    else:
        pyautogui.alert(title= 'ERRO', text='Todos os campos são obrigatórios!')

def venda():
    # Pega valores colocados nos inputs
    v_item = str(tb_item2.get())
    v_quant = tb_quantity2.get()

    # Se os inputs não forem vazios
    if tb_item2.get() and tb_quantity2.get() != "":
        # Abre o arquivo
        book = openpyxl.load_workbook("feira.xlsx")
        # Seleciona a planilha desejada
        itens_page = book['Venda']
        # Adiciona (OBS: Ele sempre adiciona na primeira linha vazia,
        # Portando, não precisa loopar.
        itens_page.append(["Maçã", 2, {dateBRL}])
        # Salva a planilha
        book.save("feira.xlsx")
        # Apaga os valores colocados nos inputs
        tb_item2.delete(0, END)
        tb_quantity2.delete(0, END)
        # Foca em um input
        tb_item2.focus()
    else:
        pyautogui.alert(title= 'ERRO', text='Todos os campos são obrigatórios!')


# Para inserir uma logo
pastaApp=os.path.dirname(__file__)

# Iniciando
app=Tk()

# Importando a logo
# logo=PhotoImage(file=pastaApp+"\\./assets/logo.png")

# Declarando os clientes
clients = ["João","Maria","Pedro","Thiago","Rafaela"]

# Configurações de clientes
inClients = StringVar()
inClients.set(clients[0])

# Data de hoje, pelo horário da sua máquina
today = date.today()
# Transforma a data para o formato Brasileiro
dateBRL = today.strftime("%d/%m/%Y")

# Coloca um pequeno icone bitmap
# app.iconbitmap(default='./assets/icon.ico')

# Título do arquivo
app.title("Cadastro de Compras")

# Coloca em tela cheia
app.state("zoomed")

# Estabelece as configurações da tela
app.configure(background="#fff")

# Criando notebooks para dividir as abas
# nb é a tela em si. Os "nb1" e "nb2" são telas dentro da tela
nb=ttk.Notebook(app)
nb.place(x=0,y=0,relwidth=1,relheight=1)

# "Compras"
nb1=Frame(nb)

# Nome da aba
nb.add(nb1,text="Compras")

# lb_logo1 = Label(nb1,image=logo).pack(fill=X)

lb_title1 = Label(nb1,text="Compra de itens", foreground="#4a9096", font="Verdana 17").pack(fill=X, pady=80)

lb_item1=Label(nb1,text="Item: ", foreground="#4a9096", font="Verdana 12", anchor="w").pack(fill=X, pady=10, padx=200, anchor="w")
tb_item1 = Entry(nb1)
tb_item1.pack(fill=X, pady=10, padx=200, anchor="w")

lb_quantity1=Label(nb1,text="Quantidade: ", foreground="#4a9096", font="Verdana 12", anchor="w").pack(fill=X, pady=10, padx=200, anchor="w")
tb_quantity1 = Spinbox(nb1, from_=1, to=50)
tb_quantity1.pack(fill=X, pady=10, padx=200, anchor="w")

tb_data1 = Label(nb1, text=dateBRL, font="Verdana 8", foreground="#4a9096").place(x=0,y=0)

Button(nb1, text="Enviar", background="#4a9096", foreground="#fff", border=2, font="Verdana 12", command=compra).pack(fill=X, pady=20, padx=500, anchor="w")

# "Vendas"
nb2=Frame(nb)

# Nome da aba
nb.add(nb2,text="Vendas")

# lb_logo2=Label(nb2,image=logo).pack(fill=X)

lb_title2=Label(nb2,text="Venda de itens", foreground="#4a9096", font="Verdana 17").pack(fill=X, pady=80)

lb_item2=Label(nb2,text="Item: ", foreground="#4a9096", font="Verdana 12", anchor="w").pack(fill=X, pady=10, padx=200, anchor="w")
tb_item2 = Entry(nb2)
tb_item2.pack(fill=X, pady=10, padx=200, anchor="w")

lb_quantity2=Label(nb2,text="Quantidade: ", foreground="#4a9096", font="Verdana 12", anchor="w").pack(fill=X, pady=10, padx=200, anchor="w")
tb_quantity2 = Spinbox(nb2, from_=1, to=50)
tb_quantity2.pack(fill=X, pady=10, padx=200, anchor="w")

lb_client2=Label(nb2,text="Cliente: ", foreground="#4a9096", font="Verdana 12", anchor="w").pack(fill=X, pady=10, padx=200, anchor="w")
drop_client2 = ttk.Combobox(nb2, value=clients)
drop_client2.bind("<<ComboboxSelected>>")
drop_client2.current(0)
drop_client2.pack(fill=X, pady=10, padx=200, anchor="w")

tb_data2 = Label(nb2, text=dateBRL, font="Verdana 8", foreground="#4a9096").place(x=0,y=0)

Button(nb2, text="SAÍDA", background="#4a9096", foreground="#fff", border=2, font="Verdana 12", command="venda").pack(fill=X, pady=20, padx=500, anchor="w")

app.mainloop()
input()
