import shutil

# diretório onde o arquivo está
FROM = r"C:\\Users\\omena\\OneDrive\\Documentações\\Transportadoras\\Transportadoras.xlsb"
# diretório onde o arquivo irá
TO = r"C:\\Users\\omena\\OneDrive\\RelatoriosDoTime\\Processos\\Rotativo"

# ele copia
shutil.copy(FROM, TO)
print("A planilha das transportadoras foi enviado a pasta 'Rotativo' com sucesso!")
print("\n")

