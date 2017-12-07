#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Q2YanSilva.py


def main():
	num=int(input("Entre com número binário\n"))
	numc=0.0
	aux=0.0
	pot=0
	ent=num
#CONVERSAO
	while(num / 10 != 0):
		aux = num % 10
		aux = aux*2**pot
		pot = pot+1
		num = num // 10
		numc = numc + aux
	print(ent,"  |  ", numc)
    

if __name__ == '__main__':
	main()
