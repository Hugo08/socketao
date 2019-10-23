import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost) Só comunica com o próprio host
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

<<<<<<< HEAD

def method_GET(arquivo):
    try:
        cabecalho = 'HTTP/1.1 200 OK\n'
        body = open(arquivo).read()                    #Tentando abrir arquivo e tentar enviar por meio do socket como string
        print('Enviado: \n',cabecalho.encode('utf-8'), body.encode('utf-8'))
        conn.send(cabecalho.encode('utf-8'), body.encode('utf-8'))                #Codificando uma string para bytes
        
    except:
        cabecalho = 'HTTP/1.1 404 NOT FOUND'
        body = 'FILE NOT FOUND 404'
        print('Enviado :\n',cabecalho, body.encode('utf-8'),)
        conn.send(body.encode('utf-8'))

def method_POST(source, content):
    try:
        arquivo = open(source, 'w')
        arquivo.write(content) 
        arquivo.close() 
        cabecalho = 'HTTP/1.1 200 OK\n'
        conn.send(cabecalho.encode('utf-8'))
    except:
        cabecalho = 'HTTP/1.1 400 ERROR'
        conn.send(cabecalho.encode('utf-8'))
    
=======
def method_GET(arquivo):   #Método GET
    try:
        cabecalho = 'HTTP/1.1 200 OK\nContent-Type: text/html\n'
        body = open(arquivo).read()                    #Tentando abrir arquivo e tentar enviar por meio do socket como string
        response = cabecalho + body
        print('Enviado: ',repr(response))
        conn.send(response.encode('utf-8'))                #Codificando uma string para bytes
        
    except:
        response = 'HTTP/1.1 404 File Not Found'
        print('Enviado ',repr(response))
        conn.send(response.encode('utf-8'))

def method_POST(arquivo):    #Método POST
    print('Nada ainda')

>>>>>>> 0bc08b2d97520498b039285cec4940bbff972e15

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
                    body = array[1]

<<<<<<< HEAD
                    if method == 'GET':
                        method_GET(source)
                    
                    if method == 'POST':
                        method_POST(source, body)
=======
                    if conection == 'HTTP/1.1':
                        if method == 'GET':
                            method_GET(source)
                        
                        elif method == 'POST':
                            method_POST(source)
                        
                        else:
                            response = 'Método errado'
                            print('Enviado: ',repr(response))
                            conn.send(response.encode('utf-8'))

                    else:
                        response = 'Servidor não suporta HTTP/1.0'
                        print('Enviado: ',repr(response))
                        conn.send(response.encode('utf-8'))
>>>>>>> 0bc08b2d97520498b039285cec4940bbff972e15

        finally:
            s.close()
            print('Conexão fechada')
