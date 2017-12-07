#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  multiplica.py


def f_multiplica(n1,n2):
	prod=0; lista1=[]; lista2=[];
	if n1 > 0 and n2 > 0:
		lista1.append(n1)
		lista2.append(n2)
		while n1 > 1:
			n1 = n1//2
			n2 = n2*2
			lista1.append(n1)
			lista2.append(n2)
		for i in range(len(lista1)):
			if (lista1[i]%2) != 0:
				prod=prod+lista2[i]			
	return prod

def main():
	i=0
	while i < 10:
		um=int(input("Insira um número positivo:\n"))
		dois=int(input("Insira outro número positivo\n"))
		if um <= 0 and dois <= 0:
			print("Valor inválido")
		else:
			prod=f_multiplica(um, dois)
			i=i+1
			print (prod)
			
if __name__ == '__main__':
	main()
		
