import socket
import threading

# Configuração do servidor
HOST = '127.0.0.1'  # IP local
PORT = 5000         # Porta para escuta

# Cria o socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f'Servidor aguardando...')

clients = []

# Envia mensagem para todos os clientes
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

# Lida com a comunicação com cada cliente
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Aceita conexões dos clientes
while True:
    client_socket, addr = server.accept()
    print(f'Conectado com {addr}')
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
