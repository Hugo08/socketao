import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost) Só comunica com o próprio host
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        
        with conn:
            print('Conectado em:', addr)
            while True:
                data = conn.recv(1024)
                data = data.decode('utf-8')          #Decodificando de bytes para string
                
                if data == '':
                    break
                
                array = data.split(' ')
                method = array[0]
                source = array[1]
                conection = array[2]
                
                '''with open('index.html','rb') as doc:           #Tentando abrir arquivo e tentar enviar por meio do socket como string
                    print(doc.read())
                    data = doc
                    doc.close()'''
                
                #print(array)

                conn.send(data)      #Codificando uma string para bytes
        s.close()
        print('Conexão fechada')