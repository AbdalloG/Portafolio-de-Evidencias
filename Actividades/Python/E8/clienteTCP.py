import argparse
import socket
from cryptography.fernet import Fernet

TCP_IP = '127.0.0.1'
TCP_PORT = 65141
BUFFER_SIZE = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (TCP_IP, TCP_PORT)
print('starting up on {} port {}'.format(*server_address))
sock.connect(server_address)

description = """Uso: 
        clienteTCP.py -msj "Mensaje a enviar"""
parser = argparse.ArgumentParser(description='Port Scanning', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-msj", metavar='MSJ', dest='msj', help="mensaje a enviar",required=True)
params = parser.parse_args()

clave = Fernet.generate_key()
suite = Fernet(clave)

mensaje = params.msj
mensajeBytes = mensaje.encode()

msj_cifrado = suite.encrypt(mensajeBytes)
print("Mensaje Enviado:\n",mensaje)
sock.sendall(msj_cifrado)
resp = sock.recv(BUFFER_SIZE).decode()
sock.close()

print("Respuesta Recibida:",resp)

file = open('clave.key', 'wb')
file.write(msj_cifrado)
file.close()