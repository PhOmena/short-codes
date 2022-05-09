import PySimpleGUI as psg

def progressBar():

    # Layout
    psg.theme('Reddit')
    layout = [
        [psg.Text('Iniciando....')],
        [psg.ProgressBar(1000, orientation='h', size=(50, 20), key='progbar')],
        [psg.Button('Cancelar', pad=(5,20), size=(20, 1))]]

    # Janela
    window = psg.Window('Carregando...', layout)
    for i in range(1000):
        eventos, valores = window.read(timeout=1)
        if eventos == 'Cancelar' or eventos == psg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()

progressBar()

# Tema
psg.theme('Reddit')

# Layout
layout = [
    [psg.Text('Senha: ', size=(15, 1)), psg.Input(key='senha', size=(40, 2), password_char="•")],
    [psg.Button('Iniciar', pad=(5,20), size=(60, 1))]]

# Título
window = psg.Window('Relatórios', layout)

# Ler os eventos
while True:
    eventos, valores = window.read()
    if eventos == psg.WINDOW_CLOSED:
        print("Processo encerrado...")
        break
    if eventos == 'Iniciar':
        if valores['senha'] != "123":
            print("Senha incorreta!")
        else:
            print("Bem vindo!")
