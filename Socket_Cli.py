import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        mensagem = input('Digite uma mensagem:' )
        s.send(mensagem.encode())
        if mensagem == '':
            break
        data = s.recv(1024)
        print('Recebido', repr(data))
    print('Fechando Conexão...')

#Estruturar a requisição e a resposta com base no protocolo http
