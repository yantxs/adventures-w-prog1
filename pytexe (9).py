#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  oi.py

def main(lista1, lista2):

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

			
if __name__ == '__main__':
	main()
