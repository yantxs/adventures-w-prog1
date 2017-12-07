#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  example.py

def buscasequencial(lst, n):
	pos=-1; achou=False; i=0; 
	while not achou  and  i<len(lst):
		if  n==lst[i]:
			achou=True; pos=i;
		i+=1
	return pos


def f_preencheSemRepeticao(qtd):
	lista=[]
	n=1
	nome=input("Entre com o nome a ser armazenado:\n").lower().capitalize()
	lista.append(nome)
	while n  < qtd:
		nome=input("Entre com o nome a ser armazenado:\n").lower().capitalize()
		if buscasequencial(lista, nome) == -1:
			lista.append(nome)
			n=n+1
		else:
			print("Nome já incluso na lista")
	return lista
	
def f_geraUniao(lista1, lista2):
	lista=[]
	lista=lista2[:]
	for i in lista1:
		if buscasequencial(lista, i) == -1:
			lista.append(i)
	return lista
	
def f_geraIersecao(lista1,lista2):
	lista=[]
	for i in lista1:
		for j in lista2:
			if i == j:
				lista.append(i)
	return lista
	
def f_imprime(lista):
	for i in range(len(lista)):
		print("pos[%d] = %s" % (i, lista[i]))

def main():
    qtd = int(input("Quantos nomes na primeira lista:\n"))
    lista1 = f_preencheSemRepeticao(qtd)
    qtd = int(input("Quantos nomes na segunda lista:\n"))
    lista2 = f_preencheSemRepeticao(qtd)
    listaU = f_geraUniao(lista1,lista2)
    listaI = f_geraIersecao(lista1,lista2)
    f_imprime(lista1)
    f_imprime(lista2)
    f_imprime(listaU)
    f_imprime(listaI)

if __name__ == '__main__':
	main()

