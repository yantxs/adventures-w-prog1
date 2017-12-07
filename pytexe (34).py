#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testexec.py

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
	
def imprimeTabela(notas, freqA, freqR):
    print("________________________")
    print("| NOTAS |FREQ A | FREQ R| ")
    print("________________________")
    for i in range(11):
        print("| {:>5.0f} | {:>5.2f} | {:>5.2f} |".format(i, freqA[i], freqR[i]))
    print("________________________")
    
def main():
	qtd=2
	nota=entnotas(qtd)
	frequenciaA=freqabsoluta(nota)
	frequenciaR=freqrelativa(nota)
	imprimeTabela(nota, frequenciaA, frequenciaR)

if __name__ == '__main__':
	main()
