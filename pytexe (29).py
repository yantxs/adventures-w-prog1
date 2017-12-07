#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  1.py

a=int(0)
pi=float(3.141592653589793238462643383279)
rep=1



while (rep == 1):
	r=float(input("Insira o raio do círculo:\n"))
	a=pi*r**2

	print("A área do círculo é:", a)

	rep=str(input("Testar novamente? (Digite sim ou não)\n"))
	if (rep == "sim" or rep == "Sim" or rep == "Si" or rep == "si" or rep == "SIM" or rep == "Si"):
		rep=1
	else:
		rep=0
	
	
	
	
	
