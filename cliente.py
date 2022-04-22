#!/usr/bin/env python3
# Glaide Lara & ovidio j S Junior 
# Servidor TCP implementado com cache 
# codigo fonte Cliente
import socket

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
s.connect(dest)

print('Para encerrar digite sair\n')
msg_input = input()
while(msg_input != 'sair'):
    s.send(msg_input.encode())
    msg_s = s.recv(1024)
    print('resposta do servidor >>>>\n',msg_s.decode(),'\n')
    msg_input = input()

s.close()