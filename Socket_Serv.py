import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost) Só comunica com o próprio host
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def method_GET(source):   #Método GET
    try:
        cabecalho = 'HTTP/1.1 200 OK\n\n'             #\nContent-Type: text/html; charset=iso-8859-1
        body = open(source).read()                    #Tentando abrir arquivo e tentar enviar por meio do socket como string
        response = cabecalho + body + '\n\n'
        print('Enviado: ',repr(response))
        conn.send(response.encode('utf-8'))                #Codificando uma string para bytes
        
    except:
        cabecalho = 'HTTP/1.1 404 Not Found\n\n'
        body = 'FILE NOT FOUND 404'
        response = cabecalho + body + '\n\n'
        print('Enviado ',repr(response))
        conn.send(response.encode('utf-8'))        

def method_POST(source, content):
    try:
        arquivo = open(source, 'w')
        arquivo.write(content) 
        arquivo.close() 
        cabecalho = 'HTTP/1.1 200 OK\n\n'
        print('Recebido ',repr(cabecalho))
        conn.send(cabecalho.encode('utf-8'))
    except:
        cabecalho = 'HTTP/1.1 400 ERROR\n\n'
        conn.send(cabecalho.encode('utf-8'))


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            
            with conn:
                print('Conectado em:', addr)
                while True:
                    data = conn.recv(1024)
                    data = data.decode('utf-8')          #Decodificando de bytes para string
                    
                    if data == '':       #Se tiver parado de mandar dados
                        break
                    
                    array = data.split(' ')
                    method = array[0]
                    source = array[1]
                    conection = array[2]
                    body = array[3]

                    if conection == 'HTTP/1.1':
                        if method == 'GET':
                            method_GET(source)
                        
                        elif method == 'POST':
                            method_POST(source,body)
                        
                        else:
                            response = 'HTTP/1.1 400 Bad Request\n\n'
                            print('Enviado: ',repr(response))
                            conn.send(response.encode('utf-8'))

                    else:
                        response = 'HTTP/1.1 505 HTTP Version Not Supported\n\n'
                        print('Enviado: ',repr(response))
                        conn.send(response.encode('utf-8'))

        finally:
            s.close()
            print('Conexão fechada')
