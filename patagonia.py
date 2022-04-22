#!/usr/bin/env python3

import socket
import random


HOST = 'localhost'
PORTA = 5002

Temp_ficticia = random.randint(1,52)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORTA))
s.listen()
print('Aguardando conexão com o cliente.../n')
# conexão e endereco
while True:
    conn, cliente = s.accept()
    print('Concetado por', cliente)
    while True:
        msg = conn.recv(1024)
        if not msg: break
        print(cliente, msg.decode())
print('Conexão realizada com', cliente)
