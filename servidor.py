#!/usr/bin/env python3

import socket

HOST = 'localhost'
PORTA = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORTA))
s.listen()
print('Aguardando conexão com o cliente.../n')
# conexão e endereco
conn, ender = s.accept()

print('Conexão realizada com', ender)
