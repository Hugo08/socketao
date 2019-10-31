import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))                                 #Iniciando conexão com HOST E PORT designadas no servidor
    while True:
        method = input('Método: ')
        source = input('Arquivo: ')
        if method == 'POST':
            body  = input('Conteúdo: ')
        else:
            body = ''
        protocol = input('Protocolo: ')
        request = method +' '+ source +' '+ protocol + ' ' + body
        s.send(request.encode('utf-8'))                     #Enviando mensagem de requisição para servidor, codificada em bytes

        response = s.recv(1024)
        response = response.decode('utf-8')                          #Decodificando de bytes para string a resposta

        array = response.split(' ')

        if array[1] != '200':
            mensagem = ''
            s.send(mensagem.encode('utf-8'))
            print('Recebido', repr(response))
            break

        print('Recebido', repr(response))

        exit = input('Deseja encerrar a conexão?(s/n)')
        if exit == 's':
            s.send(b'')
            break
    
    print('Fechando Conexão...')

#Estruturar a requisição e a resposta com base no protocolo http
