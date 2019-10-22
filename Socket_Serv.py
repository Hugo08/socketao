import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost) Só comunica com o próprio host
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def method_GET(arquivo):
    try:
        cabecalho = ''
        body = open(arquivo).read()                    #Tentando abrir arquivo e tentar enviar por meio do socket como string
        print('Enviado: ', body.encode('utf-8'))
        conn.send(body.encode('utf-8'))                #Codificando uma string para bytes
        
    except:
        body = 'FILE NOT FOUND 404'
        print('Enviado ',body.encode('utf-8'))
        conn.send(body.encode('utf-8'))

def method_POST(arquivo):
    #print('Nada ainda')


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

                    if method == 'GET':
                        method_GET(source)
                    
                    if method == 'POST':
                        method_POST(source)

        finally:
            s.close()
            print('Conexão fechada')
