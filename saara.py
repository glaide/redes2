#!/usr/bin/env python3
# Glaide Lara & ovidio j S Junior 
# Servidor TCP implementado com cache 
# codigo fonte Servidor


#depois que fizer funcionar com esse funciona com outros 2 servidores
import socket
import random

HOST = 'localhost'
PORTA = 5006
msg_r= 'reflesh'

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
        if msg.decode() == msg_r:
            conn.send(str(Temp_ficticia).encode())
            Temp_ficticia = random.randint(1,52)

print('Conexão realizada com', cliente)
