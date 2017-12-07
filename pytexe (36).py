#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  matriz.py



def criaMatriz(l, c):
	matriz=[]
	for i in range(l):
		linha=[]
		print ("\n")
		print ("{}ª linha\n".format(i+1))
		for j in range(c):
			linha.append(int(input("Insira o termo da {}ª coluna: ".format(j+1))))
		matriz.append(linha)
	return matriz
    
def somaMatriz(matriz):
	l=len(matriz)
	c=len(matriz[0])
	#linhas
	somaLin=[]
	for i in range(l):
		somal=0
		for j in range(c):
			somal+=matriz[i][j]
		somaLin.append(somal)
	
	#colunas
	somaCol=[]
	for j in range(c):
		somac=0
		for i in range(l):
			somac+=matriz[i][j]
		somaCol.append(somac)
		
	return somaLin, somaCol
	
def transpoeMatriz(matriz):
	l=len(matriz); c=len(matriz[0]);
	x=0
	trans=[]
	while c!=0:
		trans.append([])
		c-=1
	for list in matriz:
		for elem in list:
			trans[x].append(elem)
			x+=1
		x=0
	return trans

def matrizQuadrada(matriz):
	l=len(matriz)
	c=len(matriz[0])
	if l == c:
		return True
	else:
		return False
		
def matrizIdentidade(matriz):
	l=len(matriz)
	if not matrizQuadrada(matriz):
		return False
	for i in range(l):
		for j in range(l):
			if i == j:
				if matriz[i][j] != 1:
					return False
			elif matriz[i][j] != 0:
				return False
	return True
		
def somaMatrizDiag(matriz):
	i=0; l=len(matriz); c=len(matriz[i])
	#linhas
	somad=0
	if c > 1:
		for i in range(l):
			somad+=matriz[i][i]
	else:
		somad+=matriz[0][0]
	return somad

def somaMatrizDiagSec(matriz):
	l=len(matriz)
	c=len(matriz[0])
    #linhas
	somad=0; j=c-1
	if c > 1:
		for i in range(l):
			somad+=matriz[i][j]
			j-=1
	else:
		somad+=matriz[l-1][c-1]
	return somad
    
def main():
	l=int(input("Insira o número de linhas da matriz: "))
	c=int(input("Insira o número de colunas da matriz: "))
	matriz=criaMatriz(l,c)
	imprimeMatriz(matriz, "MATRIZ")
	somal,somac=somaMatriz(matriz)
	somamatdiag=somaMatrizDiag(matriz)
	somamatdiag2=somaMatrizDiagSec(matriz)
	print("{} soma das respectivas linhas|{} soma das respectivas colunas\n".format(somal,somac))
	print ("A soma da diagonal principal e da secundária são respectivamente: {} e {}\n".format(somamatdiag, somamatdiag2))
	if matrizQuadrada(matriz): print("Esta matriz é uma matriz quadrada") 
	else: print("Esta matriz não é uma matriz quadrada") 
	if matrizIdentidade(matriz): print("É uma matriz identidade") 
	else: print("Não é uma matriz identidade")
	matriztrans=transpoeMatriz(matriz)
	matriztrans=transpoeMatriz(matriz)
	imprimeMatriz(matriztrans, "MATRIZ TRANSPOSTA")

def imprimeMatriz(matriz, nome):
	linha=""
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			linha+="{} ".format(matriz[i][j])
		linha+="\n"
	print ("\n")
	print (nome)
	print (linha)

def matrizTriangular(matriz):
	somat=0; i=0; j=0;
	l=len(matriz); c=len(matriz[i]);somat=0; i=1; j=0; aux=0 
	if matrizQuadrada:
		for x in range(len(matriz)-1):
			aux+=1; j=0;
			for i in range(aux,l):
				somat+=matriz[i][j]
				j+=1
		return somat
	else:
		return False
					
def teste():
	matriz=[[1,2,9,10],[4,5,6,3],[1,2,3,2],[3,4,5,1]]
	matrizdiag=matrizTriangular(matriz)
	print (matrizdiag)
	imprimeMatriz1(matriz)	

if __name__ == '__main__':
	main()

	
