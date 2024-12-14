#FTP - File Transfer Protocol 
from ftplib import *

ftp = FTP("ftp.ibge.gov.br")
#ftp = FTP("ftp.ibiblio.org")

print(ftp.getwelcome)

# for () >>  se tiver uma lista de poss´veis usuários e possíveis senhas 
usuario = input("Informe usuário: ")
senha = input("Informe senha: ")

ftp.login(usuario,senha)

print("Pasta atual: ", ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()
