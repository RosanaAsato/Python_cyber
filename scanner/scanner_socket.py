from socket import *
import time 

# Pegar o tempo inicial 
tempo_inicial = time.time()

alvo = input("Informe o IP pra ser escaneado: ")

ip_alvo = gethostbyname(alvo)

print("Começando scan: ", ip_alvo)

#Threding (permite varias tarefas ao memo tempo)
for i in range(50, 500):
    #IPv4
    #TCP
    s = socket(AF_INET, SOCK_STREAM)

    # tento me conectar na porta 
    conexao = s.connect_ex((ip_alvo,i))

    if conexao ==0:
        print("Porta: ", i, "aberta!")

    s.close()

print("Tempo que levou: ", time.time() - tempo_inicial)