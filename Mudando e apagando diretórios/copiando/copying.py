import shutil

def copiandoArquivo():
    try:
        # Diretório onde o arquivo está
        FROM = r"C:\\Users\\omena\\OneDrive\\Documentações\\Transportadoras\\Transportadoras.xlsb"

        # Diretório onde o arquivo irá
        TO = r"C:\\Users\\omena\\OneDrive\\RelatoriosDoTime\\Processos\\Rotativo"
        
        # Ele copia
        shutil.copy(FROM, TO)
        print("A planilha das transportadoras foi enviado a pasta 'Rotativo' com sucesso!")
        print("\n")

    except:
        print("Não foi possível")

copiandoArquivo()