#!/usr/bin/env python3
# Glaide Lara & ovidio j S Junior 
# Servidor TCP implementado com cache 
# codigo fonte Servidor cache

import socket
import time

def tabela_cache():
    #implementar verificacao do campo tempo
    #implementar atualizar enviando requisição pros 3 servidores
    #acho que vai ser uma boa a gente usar uma lista de lista
    # lista [[saara,temperatura,validade],[patagonia,temperatura,validade]....]

HOST = 'localhost'
PORTA = 5000
msg_r= 'reflesh'
msg_t= 'tempo'
time_ini = time.time()

HOST_Saara = '127.0.0.1'     # Endereco IP do Servidor
PORT_Saara = 5006           # Porta do servidor SAARA

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORTA))
s.listen()

#conecta ao servidor de temperaturas Saara
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST_Saara, PORT_Saara)
s1.connect(dest)

print('Aguardando conexão com o cliente.../n')
while True:
    # conexão e endereco
    conn, cliente = s.accept()
    print('Concetado por', cliente)

    while True:
        msg_c = conn.recv(1024)
        if not msg_c: break
        if msg_c.decode() == msg_t:
            #procuro o tempo
            #verifico se esta valido
            #se estiver valido envia
            #se nao atualiza e depois envia
            s1.send(msg_r.encode())
            msg_saara = s1.recv(1024)
            print(msg_saara.decode())

print('Conexão realizada com', cliente)
