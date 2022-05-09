import PySimpleGUI as psg

# tema
psg.theme('Reddit')

# layout
layout = [
    [psg.Text('Usuário: ', size=(15, 1)), psg.Input(key='user', size=(40, 2))],
    [psg.Text('Senha: ', size=(15, 1)), psg.Input(key='password', size=(40, 2), password_char="•")],
    [psg.Button('Iniciar', pad=(5,20), size=(60, 1))]]

# título
window = psg.Window('Relatórios', layout)

# ler os eventos
while True:
    eventos, valores = window.read()
    # se a janela for fechada
    if eventos == psg.WINDOW_CLOSED:
        print("Processo encerrado...")
        break
    # se chamar o evento "iniciar"
    if eventos == 'Iniciar':
        if valores['password'] != "123":
            print("Senha incorreta!")
        else:
            print("Bem vindo!")
