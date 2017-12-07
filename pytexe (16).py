#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testeexec.py

def buscasequencial(lst, n):
	pos=-1; achou=False; i=0; 
	while not achou  and  i<len(lst):
		if  n==lst[i]:
			achou=True; pos=i;
		i+=1
	return pos

def preencheListaSemRepetir(lst, qtd):
	flag=1
	lst.append(int(input("Entre com o numero\n")))
	while flag < qtd:
		n=int(input("Entre com o numero\n"))
		if buscasequencial(lst, n) == -1:
			lst.append(n)
			flag+=1
		else:
			print ("Numero ja existente na lista. Entre com um novo numero.")

def main():
	lst=[]
	qtd=int(input("Quantos termos deseja inserir?\n"))
	preencheListaSemRepetir(lst, qtd)
	
	
			
if __name__ == '__main__':
	main()

