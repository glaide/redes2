#!/usr/bin/env python3
# Glaide Lara & ovidio j S Junior 
# Servidor TCP implementado com cache 
# codigo fonte Servidor cache

import socket
import time

#atualiza tabela cache
def atualiza_tabela_cache():
    global temperaturas
    global saara
    global msg_saara
    global msg_r
    new_time = time.time ()
    if (new_time-temperaturas[0][2])>30:
        print('temperatura do saara desatualizada, atualizando...\n')
        saara.send(msg_r.encode())
        msg_saara = saara.recv(1024)
        print('nova temperatura para saara: ',msg_saara.decode())
        temperaturas[0][1] = int(msg_saara.decode())
        temperaturas[0][2] = time.time()
    else:
         print('temperatura saara esta atualizado: ',msg_saara.decode())   

#inicializa tabela cache
def inicia_tabela_cache():
    
    saara = ['SAARA',0,30]
    patagonia = ['patagonia',0,30]
    terceiro = ['terceiro',0,30]
    lista_temp = list()
    lista_temp.append(saara)
    lista_temp.append(patagonia)
    lista_temp.append(terceiro)
    return lista_temp

#organiza a mensagem para o cliente
def monta_msg():
    global temperaturas
    msg = str(temperaturas[0][0])
    msg = msg+': '+ str(temperaturas[0][1])

    msg = msg+'\n'+ str(temperaturas[1][0])
    msg = msg+': '+ str(temperaturas[1][1])

    msg = msg+'\n'+ str(temperaturas[2][0])
    msg = msg+': '+ str(temperaturas[1][1])+ '\n'

    return msg
###################Programa principal#############################

HOST = 'localhost'
PORTA = 5000
msg_r= 'reflesh'
msg_t= 'tempo'
time_ini = time.time()
temperaturas = inicia_tabela_cache()

HOST_Saara = '127.0.0.1'     # Endereco IP do Servidor
PORT_Saara = 5006           # Porta do servidor SAARA

#################Conexao para o cliente #########################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen()

#################Conexao para o servidor Saara ##################

saara = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST_Saara, PORT_Saara)
saara.connect(dest)

print('Aguardando conexão com o cliente...\n')
while True:
    # conexão e endereco
    conn, cliente = s.accept()
    print('Conectado por', cliente)

    while True:
        msg_c = conn.recv(1024)
        if not msg_c: break
        if msg_c.decode() == msg_t:
            atualiza_tabela_cache()
            msg_c = monta_msg()
            conn.send(msg_c.encode())

print('Conexão realizada com', cliente)
