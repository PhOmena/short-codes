from imap_tools import MailBox, AND
import time
import pyautogui

#### LEMBRANDO DE ACEITAR O IMAP NOS EMAILS ####

# Essa função busca o e-mail de estoque no Gmail e faz o download do anexo.

# Seu email
email = ""
# Senha do email
password = ""

# Indicando que a caixa é do tipo Gmail, para fazer o login
myMailBox = MailBox('imap.gmail.com').login(email, password)
# Acessa a caixa de entrada e define quais emails procurar
emailsList = myMailBox.fetch(AND(from_="anyemail@gmail.com"))

for email in emailsList:
    # Se existir anexo ->
    if len(email.attachments) > 0:
        # E para cada um deles
        for anexo in email.attachments:
            # Se o nome aparece no anexo ele carrega
            if 'anexo' in anexo.filename:
                print(anexo.content_type)
                print(anexo.payload)

                # Fara o download em bits do arquivo com o nome especificado abaixo
                with open("novoAnexo.xlsx", 'wb') as arquivo_excel:
                    arquivo_excel.write(anexo.payload)
                print('Relatório extraído com sucesso :)')
    else:
        pyautogui.alert('Não foi possível extrair o relatório :(')

# Tempo do download do anexo ser concluído. Sempre tomar cuidado com isso
time.sleep(5)