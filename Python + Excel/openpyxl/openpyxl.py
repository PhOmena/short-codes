import openpyxl

# Abre o arquivo
book = openpyxl.load_workbook("*arquivo*.xlsx")
# Vai até a planilha desejada
itens_page = book['Plan1']
# Adiciona itens
itens_page.append(["20/02/2020","Saída","Maçã","2"])
# Salva a planilha
book.save("*arquivo*.xlsx")

