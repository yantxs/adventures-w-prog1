#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testeexec.py

# 8 8 9 5 6 7 9 10 10

def entnotas(qtd):
	lista=[]
	for i in range(qtd):
		nota=int(input("Insira a nota do aluno:"))
		lista.append(nota)
	return lista

def freqabsoluta(lst):
	i=0; lista=[0,0,0,0,0,0,0,0,0,0,0];
	for i in range(len(lst)):
		lista[lst[i]] += 1
	return lista
	
def freqrelativa(lst):
	lista=freqabsoluta(lst)
	lista2=[]
	for i in lista:
		x=i/len(lst)
		lista2.append(x)
	return lista2
	
def imprime(lst):
	print(lst)

def main():
	qtd=8
	alunos=entnotas(qtd)
	frequenciaA=freqabsoluta(alunos)
	frequenciaR=freqrelativa(alunos)
	imprime(alunos)
	imprime(frequenciaA)
	imprime(frequenciaR)

if __name__ == '__main__':
	main()
