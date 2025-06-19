import socket
import threading

# Configuração do cliente
HOST = '127.0.0.1'
PORT = 5000

# Conecta ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Recebe mensagens do servidor
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Conexão encerrada.")
            client.close()
            break

# Envia mensagens ao servidor
def send_messages():
    while True:
        message = input('')
        client.send(message.encode())

# Cria e inicia as threads
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
