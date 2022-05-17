import socket 
from cryptography.fernet import Fernet

TCP_IP = '127.0.0.1' 
TCP_PORT = 65141 
BUFFER_SIZE = 2048 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (TCP_IP, TCP_PORT)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    print('Esperando Conexion...')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        msj_cifrado = connection.recv(BUFFER_SIZE)
        if msj_cifrado:
                connection.sendall(msj_cifrado)
        else:
                print('no data from', client_address)
                break
    finally:
        print (b"Enterado. Bye!")
        connection.close()

archi = open('clave.key', 'rb')
clave = archi.read()
archi.close()
cipher_suite = Fernet(clave)

mensajeB = cipher_suite.decrypt(msj_cifrado,None)
mensaje = mensajeB.decode()
print('Mensaje Recibido:\n',mensaje)