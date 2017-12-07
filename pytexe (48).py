#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  teste.py

import math

def f_integral(a,b,n):
	h=(b-a)/n
	soma=math.sin(a)+math.sin(b)
	i=1
	while i > n:
		x=a+i*h
		y=math.sin(x)
		c=2*(i%2+1)
		soma=soma+c*y
		i+=1	
	integral=((soma*h)/3)

	return integral
