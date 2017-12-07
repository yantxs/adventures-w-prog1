#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bbanco.py

import os
clear = lambda: os.system('cls')
import time
import locale



montante=0.0
op = 1



def voltar():
	back=1
	back=int(input("[0]Voltar ao menu anterior\n"))
	
def deposito():
	clear()
	global montante
	dep=0.0
	dep=float(input("Quantia a ser depositada:"))
	clear()
	if (dep > 0):
		print (" |",montante)
		print ("+|",dep)
		montante=montante+dep
		print ("____________")
		print (" |",montante,"\n\n")
	else:
		print("Quantia inválida")
	voltar()
	return montante
	
def saldo():
	clear()
	print ("O seu saldo é:","%2.2f%%", montante)
	voltar()
	
def saque():
	clear()
	global montante
	while True:
		clear()
		saq=0.0
		saq=float(input("Quantia a ser sacada:"))
		if(saq <= montante):
			print (" | R$ :.2f.",montante)
			print ("-| R$ :.2f.",saq)
			montante=montante-saq
			print ("____________")
			print (" | R$ :.2f.",montante,"\n\n")
			break
		else:
			clear()
			print("Saldo insuficiente")
			time.sleep(1)
			voltar()
	return montante	

def main():
	while True:
		clear()
		print("Qual tipo de operação deseja realizar?\n")
		print ("[1]Saldo")
		print ("[2]Depósito")
		print ("[3]Saque")
		print ("[0]Sair\n")
		op=int(input())
		
		
		if(op == 1):
			saldo()
		elif(op == 2):
			deposito()
		elif(op == 3):
			saque()
		elif(op == 0):
			break
		else:
			clear()
			print("Operação inválida")
			time.sleep(1)	

if __name__ == '__main__':
	main()
