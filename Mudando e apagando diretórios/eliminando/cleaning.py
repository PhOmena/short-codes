import os

# diretório
REPORT = r"C:\\Users\\omena\\OneDrive\\RelatoriosDoTime\\Processos\\"

# seleciona o diretório
os.chdir(REPORT)

# Para cada arquivo {f} no diretório especificado, ele remove
for f in os.listdir():
    os.remove(f)
    print(f"{f} removido com sucesso!")
