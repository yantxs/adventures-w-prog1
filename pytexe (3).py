#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  oi.py

def main():
	
	lista=[2.5,3.1,7.1,9.5,10.5]
	maximo=lista[0]
	minimo=lista[0]
	
	for e in lista:
		if e > maximo:
			maximo = e
	for e in lista:
		if e < minimo:
			minimo = e
			
	soma=maximo+minimo
	print(soma)

			
if __name__ == '__main__':
	main()
