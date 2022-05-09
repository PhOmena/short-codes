import openpyxl

# abre o arquivo
book = openpyxl.load_workbook("arquivo.xlsx")
# vai até a planilha desejada
itens_page = book['Plan1']
# adiciona itens
itens_page.append(["20/02/2020","Saída","Maçã","2"])
# salva a planilha
book.save("arquivo.xlsx")

print('Informações armazenadas com sucesso :)')

