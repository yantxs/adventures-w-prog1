#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ordem.py



def ordenar(lista):
	i=0
	aux=""
	x=1
	
	for i in range(len(lista)):
		for i in range(len(lista)-1):
			if lista[i] > lista [i+1]:
				aux=lista[i]
				lista[i]=lista[i+1]
				lista[i+1]=aux
				x +=1			
	return lista
