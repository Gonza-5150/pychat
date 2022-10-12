import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, post))
server.listen()
print(f"server running on {host}:{port}")

clients = []
usernames = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)



def handle_message(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, _client)
        except:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f"ChatBot: {username} disconected".encode('utf-8'))
            clients.remove(client)
            usernames.remove(username)
            client.close()

def recive_connections():
    client, addres = server.accept()
    client.send("@username".encode('utf-8'))
    username = client.recv(1024).decode('utf-8')

    clients.append(client)
    usernames.append(username)

    print(f"{username}is connected with {str(addres)}")
    