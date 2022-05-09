import PySimpleGUI as psg

# layout
psg.theme('Reddit')
layout = [
    [psg.Text('Iniciando....')],
    [psg.ProgressBar(1000, orientation='h', size=(50, 20), key='progbar')],
    [psg.Button('Cancelar', pad=(5,20), size=(20, 1))]]

# janela
window = psg.Window('Carregando...', layout)
for i in range(1000):
    eventos, valores = window.read(timeout=1)
    # se for igual a cancelar
    if eventos == 'Cancelar' or eventos == psg.WIN_CLOSED:
        break
    window['progbar'].update_bar(i + 1)
window.close()
