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
    msg_r = 'reflesh'
    new_time = time.time ()

    if (new_time-temperaturas[0][2])>30:
        print('temperatura do saara desatualizada, atualizando...')
        saara.send(msg_r.encode())
        msg_saara = saara.recv(1024)
        print('nova temperatura para saara: ',msg_saara.decode(),'\n')
        temperaturas[0][1] = int(msg_saara.decode())
        temperaturas[0][2] = time.time()
    else:
         print('temperatura saara esta atualizado: ',temperaturas[0][1],'\n')

    if (new_time-temperaturas[2][2])>30:
        print('temperatura do patagonia desatualizada, atualizando...')
        patagonia.send(msg_r.encode())
        msg_patagonia = patagonia.recv(1024)
        print('nova temperatura para patagonia: ',msg_patagonia.decode(),'\n')
        temperaturas[2][1] = int(msg_patagonia.decode())
        temperaturas[2][2] = time.time()
    else:
         print('temperatura patagonia esta atualizado: ',temperaturas[2][1],'\n')   
         
    if (new_time-temperaturas[1][2])>30:
        print('temperatura do antartida desatualizada, atualizando...')
        antartida.send(msg_r.encode())
        msg_antartida = antartida.recv(1024)
        print('nova temperatura para antartida: ',msg_antartida.decode(),'\n')
        temperaturas[1][1] = int(msg_antartida.decode())
        temperaturas[1][2] = time.time()
    else:
         print('temperatura antartida esta atualizado: ',temperaturas[1][1],'\n')


##############Inicializa tabela cache##############################

def inicia_tabela_cache():
    saara = ['Saara',0,30]
    patagonia = ['Patagonia',0,30]
    antartida = ['Antartida',0,30]
    lista_temp = list()
    lista_temp.append(saara)
    lista_temp.append(patagonia)
    lista_temp.append(antartida)
    return lista_temp

############Organiza a mensagem para o cliente#####################
def monta_msg():
    global temperaturas
    msg = str(temperaturas[0][0])
    msg = msg+': '+ str(temperaturas[0][1])

    msg = msg+'\n '+ str(temperaturas[1][0])
    msg = msg+': '+ str(temperaturas[1][1])

    msg = msg+'\n '+ str(temperaturas[2][0])
    msg = msg+': '+ str(temperaturas[2][1])+ '\n'

    return msg

###################Definições do Servidor ########################

HOST = 'localhost'
PORTA = 5000
msg_t= 'tempo'
temperaturas = inicia_tabela_cache()

HOST_saara = '127.0.0.1'     # Endereco IP do Servidor
PORT_saara = 5001          # Porta do servidor SAARA

HOST_antartida = '127.0.0.1'     # Endereco IP do Servidor
PORT_antartida = 5002           # Porta do servidor SAARA

HOST_patagonia = '127.0.0.1'     # Endereco IP do Servidor
PORT_patagonia = 5003           # Porta do servidor SAARA

#################Conexao para o cliente #########################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen()

#################Conexao para o servidor Saara ##################

saara = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST_saara, PORT_saara)
saara.connect(dest)

#################Conexao para o servidor Antartida ##################

patagonia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST_patagonia, PORT_patagonia)
patagonia.connect(dest)

#################Conexao para o servidor Patagonia ##################

antartida = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST_antartida, PORT_antartida)
antartida.connect(dest)

###################Programa principal#############################

print('Aguardando conexão com o cliente...\n')
while True:
    conn, cliente = s.accept()  # conexão e endereco
    print('Conectado por', cliente)

    while True:
        print('Aguardando requisição do cliente : \n')
        msg_c = conn.recv(1024)
        if not msg_c: break
        if msg_c.decode() == msg_t:
            atualiza_tabela_cache()
            msg_c = monta_msg()
            conn.send(msg_c.encode())

