#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inv.py



def main():	
	num=0
	alg=0
	soma=0
	again="sim"
	import time
#PROGRAMA
	while(again == "sim" or again == "Sim" or again == "SIM"):
		num=int(input("Insira o número a ser invertido\n"))
		while(num > 0):
			alg = num % 10
			soma=soma*10+alg
			alg = num // 10
			num=num//10
		print (soma)
		again=str(input("Deseja testar outro número? (Responda sim ou não)\n"))
		soma=0
		if(again == "Não" or again == "não" or again == "NÃO"):
			time.sleep(0.2)
			print("Finalizando o programa")
			time.sleep (0.1)

if __name__ == '__main__':
    main()
