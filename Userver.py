import socket
import sys
import os.path

def server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the port
    HOST='localhost'
    PORT=10000
    server_address = (HOST, PORT)
    print(f"iniciando no {HOST} na porta {PORT}")
    sock.bind(server_address)
    while True:
        arquivo=open("postos.txt", "w")
        print("Tentando estabelecer conexão")
        recebidos=sock.recvfrom(4096)
        mensagemRecebida=recebidos[0]
        endereco=recebidos[1]
        texto=mensagemRecebida.decode('utf-8')
        try:
            arquivo.write(texto)
            arquivo.flush() 
            arquivo.flush()
        except Exception as e:
            print(f"Erro {e.__class__} ocorreu")

        dados=f"foi recebido {texto}"
        print(dados)
        sock.sendto(bytes(dados,'utf-8'), endereco)

    arquivo.close()
    sock.close()

server()