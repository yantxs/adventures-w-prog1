#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  entradabuscaseq.py

lista = []

def preencheLista(lista,taml):
	for i in range(taml):
		duplicidade = True
		while duplicidade:
			c=float(input("Entre com o termo\n"))
			lista.append(c)
			for i in range(len(lista)):
				if c == lista[i]:
					duplicidade = True
				else:
					duplicidade = False		
			if duplicidade and i != 0:
				print ("Valor ja existente, digite um novo valor")
			else:
				lista.append(c)	
				
	print (lista)
#print ("Valor ja existente, digite um novo valor")

if __name__ == '__main__':
	preencheLista(lista, 10)
