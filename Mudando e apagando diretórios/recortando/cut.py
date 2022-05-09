import os

def renameInventory():

    # Diretório onde o arquivo está
    FROM = r"C:\\Users\\omena\\OneDrive\\Analise\\"

    # Diretório para onde o arquivo irá
    TO = r"C:\\Users\\omena\\OneDrive\\Analise\\Dados\\"

    # Indo até o diretório
    os.chdir(FROM)

    # Para cada arquivo, se ele tiver o nome ou extensão "xlsx" ele move
    for f in os.listdir():
        if ".xlsx" in f:
            os.rename(f,TO + f)
            print(f'Relatório {f} movido para "Dados" com sucesso!')

renameInventory()
