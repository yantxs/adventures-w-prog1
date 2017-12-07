#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  npo.py

def main():
#VARIAVEIS

	a=0.0
	b=0.0
	c=0.0
	delta=0.0
	x1=0.0
	x2=0.0
while True:
	a=float(input("Insira o valor de A\n"))
	b=float(input("Insira o valor de B\n"))
	c=float(input("Insira o valor de C\n"))
	delta=float
	x1=float
	x2=float
	delta=(b**2)-(4*a*c)

	#PROGRAMA
	if (a != 0 and delta >= 0):
		x1=(-b+delta**0.5)/2*a
		x2=(-b-delta**0.5)/2*a
		print("O valor de x' e x'', são respectivamente:", x1,x2)
	elif (delta < 0):
		print("Solução no domínio dos números complexos")
		x1=(-b+delta**0.5)/2*a
		x2=(-b-delta**0.5)/2*a
		print("O valor de x' e x'', são respectivamente:", x1,x2)

	if (a == 0 and b != 0):
		x1=c/b
		print('O valor de x é:',x1)
	elif(b == 0 and c == 0):
		print("Qualquer valor de x satisfaz a igualdade")
	elif(b == 0 and c != 0):
		print("Nenhum valor de x satisfaz a igualdade")



if __name__ == '__main__':
	main()
