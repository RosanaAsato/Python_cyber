from socket import *

endereco = "127.0.0.1"
porta = 43210

while True:
    #IPv4 e o IPv6
    #AF_INET = IPv4

    #TCP ou UDP
    #TCP - mais segura 
    #UDP - Menos segura e mais rapida
    # SOCK_STREAM = TCP 
    obj_socket = socket(AF_INET,SOCK_STREAM)
    obj_socket.connect((endereco,porta))
    msg = bytes(input("Mensage: "), 'utf-8')

    obj_socket.send(msg)

    resposta = obj_socket.recv(1024)
    print("Resposta: ", str(resposta)[2:-1])
    if str(msg)[2:-1] == "fim":
        break
obj_socket.close()