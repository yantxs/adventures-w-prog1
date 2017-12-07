# -*- coding: utf-8 -*-
#!/usr/bin/python3
import socket
# nao tem servidor UDP no google -> vamos usar netcat como servidor UDP!
#Programa de chat: so fala um de cada vez
#implementar falando ao mesmo tempo

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

"""
pacotes_recebidos = client.recvfrom(1024) devolve uma tupla:
(' llallalaaaa\n', ('192.168.1.4', 667))

msg recebida + (IP,porta)
"""
try:    
    while 6: #while True
        #client.sendto(input("Voce: ") + "\n", ("192.168.1.4", 668))
        #client.sendto (bytes(input("Voce: ")).encode('utf8') + bytes("\n").encode('utf8'), bytes(("192.168.1.4", 668)).encode('utf8'))
        client.sendto((input("Voce: ")).encode('utf8') + ("\n").encode('‌​utf‌​8'),("127.0.0.1", 661))
        # endereço do servidor UDP do kali linux usando netcat
        msg, friend = client.recvfrom(1024)
        print(str(friend) + ": " + str(msg))
 #se quiser apenas o ip: use friend[0]

    client.close()

except Exception as erro:
    print("Conexao falhou ")
    print("O erro foi: ", erro)
    client.close()
