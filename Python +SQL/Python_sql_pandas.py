import pandas as pd
import pyodbc
import time

try:
    # Passa os dados da conexão
        # Driver = Se for SQL, SQL Server, caso seja outro, pesquisar
        # Server = Numero do server ou se tiver local, nome do dispositivo - Exemplo: "Desktop-2342H"
        # Database = Nome da base de dados que você quer consultar ou implementar
    dados_conexao = ("Driver={SQL Server};""Server=10.100.48.9;""Database=BaseServico;")

    # Fazendo a conexão com o servidor
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão com o servidor estabelecida com sucesso!")
    time.sleep(3)

    # Utilizando o PANDAS para ler o SQL
    totalDataBase = pd.read_sql('SELECT * FROM BaseServico.dbo.*nome_da_tabela*', conexao)
    print("Informação encontrada")
    time.sleep(5)

    # Importando para um CSV
    totalDataBase.to_csv("./arquivo.csv", index=False)
except:
    print("Não foi possível")


