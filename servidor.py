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

    if (new_time-temperaturas['Saara'][1])>30:
        print('temperatura do saara desatualizada, atualizando...')
        try:
            saara.send(msg_r.encode())
            msg_saara = saara.recv(1024)
            print('nova temperatura para saara: ',msg_saara.decode(),'\n')
            temperaturas['Saara'][0] = int(msg_saara.decode())
            temperaturas['Saara'][1] = time.time()
        except:
            print('servidor saara pode ter desconectado','\n')
    else:
         print('temperatura saara esta atualizado: ',temperaturas['Saara'][0],'\n')

    if (new_time-temperaturas['Patagonia'][1])>30:
        print('temperatura do patagonia desatualizada, atualizando...')
        try:
            patagonia.send(msg_r.encode())
            msg_patagonia = patagonia.recv(1024)
            print('nova temperatura para patagonia: ',msg_patagonia.decode(),'\n')
            temperaturas['Patagonia'][0] = int(msg_patagonia.decode())
            temperaturas['Patagonia'][1] = time.time()
        except:
            print('servidor patagonia pode ter desconectado','\n')
            
    else:
         print('temperatura patagonia esta atualizado: ',temperaturas['Patagonia'][0],'\n')   
         
    if (new_time-temperaturas['Antartida'][1])>30:
        print('temperatura do antartida desatualizada, atualizando...')
        try:
            antartida.send(msg_r.encode())
            msg_antartida = antartida.recv(1024)
            print('nova temperatura para antartida: ',msg_antartida.decode(),'\n')
            temperaturas['Antartida'][0] = int(msg_antartida.decode())
            temperaturas['Antartida'][1] = time.time()
        except:
            print('servidor antartida pode ter desconectado','\n') 
    else:
         print('temperatura antartida esta atualizado: ',temperaturas['Antartida'][0],'\n')


##############Inicializa tabela cache##############################

def inicia_tabela_cache():
    temperaturas = {'Saara': [0,30], 'Patagonia': [0,30], 'Antartida': [0,30]}
    return temperaturas

############Organiza a mensagem para o cliente#####################
def monta_msg():
    new_time = time.time ()
    global temperaturas
    msg = 'Saara '
    msg = msg+': '+ str(temperaturas['Saara'][0])
    if (new_time-temperaturas['Saara'][1])>30:
        msg = msg+' (desatualizado)'

    msg = msg+'\n '+ 'Patagonia '
    msg = msg+': '+ str(temperaturas['Patagonia'][0])
    if (new_time-temperaturas['Patagonia'][1])>30:
        msg = msg+' (desatualizado)'

    msg = msg+'\n '+ 'Antartida '
    msg = msg+': '+ str(temperaturas['Antartida'][0])
    if (new_time-temperaturas['Antartida'][1])>30:
       msg = msg+' (desatualizado)'

    return msg

###################Definições do Servidor ########################

HOST = 'localhost'
PORTA = 5000
msg_t= 'tempo'
temperaturas = inicia_tabela_cache()

HOST_saara = '127.0.0.1'     # Endereco IP do Servidor
PORT_saara = 5001          # Porta do servidor SAARA

HOST_antartida = '127.0.0.1'     # Endereco IP do Servidor
PORT_antartida = 5002           # Porta do servidor ANTARTIDA

HOST_patagonia = '127.0.0.1'     # Endereco IP do Servidor
PORT_patagonia = 5003           # Porta do servidor PATAGONIA

#################Conexao para o cliente #########################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen()

#################Conexao para o servidor Saara ##################

saara = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST_saara, PORT_saara)
try:
    saara.connect(dest)
except:
    print("Conexao com servidor Saara falhou")
    
#################Conexao para o servidor Antartida ##################

patagonia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST_patagonia, PORT_patagonia)
try:
    patagonia.connect(dest)
except:
    print("Conexao com servidor Patagonia falhou")
    
#################Conexao para o servidor Patagonia ##################

antartida = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST_antartida, PORT_antartida)

try:
    antartida.connect(dest)
except:
    print("Conexao com servidor Antartida falhou")

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
        else:
            msg_c = 'tente outro comando'
            conn.send(msg_c.encode())

