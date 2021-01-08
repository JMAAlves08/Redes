import socket
import sys

def insercao():
    dado=""
    tmp=input("(0)-Diesel, (1)-Álcool, (2)-Gasolina\n")
    if(tmp=='0' or tmp=='1' or tmp=='2'):
        dado+=tmp+" "
        tmp=input("Preço: \n")
        tmp=float(tmp)
        dado+=str(int(tmp*1000))+" "
        tmp=input("Lat: \n")
        tmp=float(tmp)
        dado+=str(tmp)+" "
        tmp=input("Long: \n")
        tmp=float(tmp)
        dado+=str(tmp)+' '
        print(f"{dado} será enviado.")
    return(dado)

def client():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 10000)
    message = 'This is the message.  It will be repeated.'
    message=insercao()

    try:

        # Receive response
        #data, server = sock.recvfrom(4096)
        #print(f"conexão estabelecida com {server}")

        # Send data
        print(f"Enviando mensagem: {message}")
        sent = sock.sendto(message.encode('utf-8'), server_address)

        # Receive response
        print("Aguardando recebimento")
        data, server = sock.recvfrom(4096)
        print(f"Recebido: {data}")

    finally:
        print("fechando")
        sock.close()


client()