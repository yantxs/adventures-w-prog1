#!/usr/bin/env python
# -*- coding: utf-8 -*-
# EXERCICIO PROPOSTO
# Yan Teixeira da Silva - 20172BSI0149
#  teste.py

#ABERTURA
def main():
#DECLARAÇÃO DE VARIAVEIS
	a, b, c, delta, x1, x2=0.0, 0.0, 0.0, 0.0, 0.0, 0.0

	a=float(input("Insira o valor de A:\n"))
	b=float(input("Insira o valor de B:\n"))
	c=float(input("Insira o valor de C:\n"))
	delta, x1, x2=float, float, float
	delta=(b**2)-(4*a*c)

	#PROGRAMA
	if (a != 0):
		if delta >=0:
			x1=(-b+delta**0.5)/2*a
			x2=(-b-delta**0.5)/2*a
			print("O valor de x' e x'', são respectivamente:", x1,x2)
		elif (delta < 0):
			print("Solução no domínio dos números complexos")
			x1=(-b+delta**0.5)/2*a
			x2=(-b-delta**0.5)/2*a
			print("O valor de x' e x'', são respectivamente:", x1,x2) 
	elif(b != 0):
		x1=c/b
		print('O valor de x é:',x1)
	elif(b == 0 and c == 0):
		print("Qualquer valor de x satisfaz a igualdade")
	elif(b == 0 and c != 0):
		print("Nenhum valor de x satisfaz a igualdade")
#END
if __name__ == '__main__':
	main()
