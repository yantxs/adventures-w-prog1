#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testt0310.py

def preencheLista(lista,taml):
	for i in range(taml):
		c=float(input("Entre com o termo\n"))
		lista.append(c)	
	return lista
	
def ordenaLista(lista):
	i=0
	aux=""	
	for i in range(len(lista)):
		for i in range(len(lista)-1):
			if lista[i] > lista [i+1]:
				aux=lista[i]
				lista[i]=lista[i+1]
				lista[i+1]=aux			
	return lista
	
def imprimeLista(lista):
	print (lista)
	
def intercalaOrdenado(lista1, lista2):
	lista3=[]
	i=0
	j=0
	while i<len(lista1) and j<len(lista2):
		if(lista1[i] < lista2[j]):
			lista3.append(lista1[i])
			i=i+1
		else:
			lista3.append(lista2[j])
			j=j+1
	if i == len(lista1):
		while j < len(lista2):
			lista3.append(lista2[j])
			j+=1
	elif j == len(lista2):
		while i < len(lista1):
			lista3.append(lista1[i])
			i+=1
	return lista3

def main():
  lista1=[]; lista2=[]; lista3=[];
  lista1 = preencheLista(lista1, 10)
  imprimeLista(lista1)
  lista2 = preencheLista(lista2, 15)
  imprimeLista(lista2)
  lista1 = ordenaLista(lista1)
  imprimeLista(lista1)
  lista2 = ordenaLista(lista2)
  imprimeLista(lista2)
  lista3 = intercalaOrdenado(lista1, lista2)
  imprimeLista(lista3)

if __name__ == "__main__":
  main()

