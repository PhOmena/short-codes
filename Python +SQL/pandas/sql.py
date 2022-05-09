import pandas as pd
import pyodbc
import time

try:
    # passa os dados da conexão
        # Driver = Se for SQL, SQL Server, caso seja outro, pesquisar
        # Server = Numero do server ou se tiver local, nome do dispositivo - Exemplo: "Desktop-2342H"
        # Database = Nome da base de dados que você quer consultar ou implementar
    dataConnection = ("Driver={SQL Server};""Server=10.100.48.9;""Database=BaseServico;")

    # fazendo a conexão com o servidor
    connection = pyodbc.connect(dataConnection)
    print("Conexão com o servidor estabelecida com sucesso!")
    time.sleep(3)

    # utilizando o PANDAS para ler o SQL
    totalBase = pd.read_sql('SELECT * FROM BaseServico.dbo.*nome_da_tabela*', connection)
    print("Informação encontrada")
    time.sleep(5)

    # importando para um CSV
    totalBase.to_csv("./arquivo.csv", index=False)
except:
    print("Não foi possível")


