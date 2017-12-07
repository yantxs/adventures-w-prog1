#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  polinomio.py

def ordenacresc(lst):
	for i in range(len(lst)):
		for i in range(len(lst)-1):
			if lst[i][0] > lst[i+1][0]:
				aux=lst[i]
				lst[i]=lst[i+1]
				lst[i+1]=aux
	return lst

def buscaseq(lst,elem):
	pos=-1 ; achou = False ; i=0
	while not achou and i<len(lst):
		if lst[i][0] == elem:
			achou = True; pos = i
		i+=1
	
	return pos
	
def criaPol(lst):
	termo=[]; i=0
	grau=int(input("Digite o grau do termo: "))
	termo.append(grau)
	while grau > 0:
		pos=buscaseq(lst,grau)
		coef=float(input("Digite o coeficiente do termo: "))
		if pos == -1:
			termo=[grau, coef]
			lst.append(termo)
		else:
			lst[pos][1]+=coef
		grau=int(input("Digite o grau do termo: "))
		i+=1
	lst=ordenacresc(lst)
		
	return lst
	
def atribuiPol(lst,x):
	soma=0.0
	for i in range(len(lst)):
		z=lst[i][1]; y=lst[i][0];
		soma+=z*(x**y)
	
	return soma
	
def derivPol(lst):
	dx=[]; termo=[];
	for i in range(len(lst)):
		coef=lst[i][1]
		grau=lst[i][0]
		if grau > 0:
			coef=grau*coef
			grau-=1
		termo=[grau, coef]
		dx.append(termo)
			
	return dx
	
def escrevePol(lst):
	i=0
	polinomio=""; 
	for i in range(len(lst)-1,-1,-1):
		coef=lst[i][1]; grau=lst[i][0];
		if coef > 0 and i != len(lst)-1:
			polinomio+="+ "
		elif coef < 0:
			polinomio+="- "
		if grau != 0:
			polinomio+="{:=}x^{} ".format(coef, grau)

	return polinomio
		
def imprimePol(lst):
	print (lst)

def main():
	pol=[]; polx=[]; pold=[];
	pol=criaPol(pol)
	pold=derivPol(pol)
	polw=escrevePol(pol)
	polw2=escrevePol(pold)
	imprimePol(polw)
	imprimePol(polw2)
	
	
	x=float(input("Insira o valor de x: "))
	polx=atribuiPol(pol,x)
	imprimePol(polx)
	
if __name__ == '__main__':
	main()
