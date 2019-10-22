import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))                                 #Iniciando conexão com HOST E PORT designadas no servidor
    while True:
        mensagem = input('Digite uma mensagem:' )
        s.send(mensagem.encode('utf-8'))                     #Enviando mensagem de requisição para servidor, codificada em bytes
        
        if mensagem == '':
            break

        data = s.recv(1024)
        data = data.decode('utf-8')                          #Decodificando de bytes para string a resposta

        print('Recebido', repr(data))
    
    print('Fechando Conexão...')

#Estruturar a requisição e a resposta com base no protocolo http
