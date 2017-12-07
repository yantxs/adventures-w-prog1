#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mercado.py

def buscaseq(lst, elem):
	pos=-1; achou=False; i=0
	while not achou and i <len(lst):
		if lst[i][0].lower == elem.lower:
			pos=i; achou=True
		i+=1
	return pos

def f_cadastrarProdutos(cadProdutos):
	prod=[]; nome=""; pcompra=0.0; pvenda=0.0; estoque=0; vend=0
	nome=input("Digite o nome do produto: ")
	while nome != "":
		aux=buscaseq(cadProdutos, nome)
		while aux != -1:
			print ("Produto já registrado.")
			nome=input("Por favor, insira um novo produto: ")
			aux=buscaseq(cadProdutos, nome)
		pcompra=float(input("Digite o preço de compra: "))
		pvenda=float(input("Digite o preço da venda: "))
		while pcompra > pvenda:
			print ("Valor inválido, preço de custo maior que o preço de venda")
			pvenda=float(input("Digite o preço da venda: "))
		estoque=int(input("Digite a quantidade em estoque: "))
		prod=[nome, pcompra, pvenda, estoque, vend]
		cadProdutos.append(prod)
		nome=input("Digite o nome do produto: ")
	return cadProdutos

def f_venderProdutos(cadProdutos):
	nome=""; prod=[]; pos=0; qtd=0;
	nome=input("Qual produto deseja comprar: ")
	while nome != "":
		if buscaseq(cadProdutos, nome) == -1:
			while buscaseq(cadProdutos, nome) == -1:
				print("Produto não cadastrado.")
				nome=input("Por favor, digite um produto válido")
				buscaseq(cadProdutos, nome)
		else:
			pos=buscaseq(cadProdutos, nome)
		
		estoque=cadProdutos[pos][3]; vend=cadProdutos[pos][4];
		qtd=int(input("Digite a quantidade a ser comprada: "))
		if qtd > (estoque-vend):
			print("Quantia em estoque insuficiente.")
		else:
			print("Compra efetuada com sucesso.")
			cadProdutos[pos][4]+=qtd
			cadProdutos[pos][3]-=qtd
		nome=input("Qual produto deseja comprar: ")
		
	return cadProdutos	

def f_imprimirRelVendas(lst):
	total=0.0
	print("{:>8}  |{:>6}".format("PRODUTO","TOTAL VENDIDO"))
	for i in range(len(lst)):
		nome=lst[i][0].capitalize; pcompra=lst[i][1]; pvenda=lst[i][2]; vend=lst[i][4];
		totvend=vend*pvenda
		total+=totvend
		if vend != 0:
			print("{:<8}  |R${:>6.2f}".format(nome, totvend))
	print("______________________")
	print("{:^8}  |R${:>6.2f}".format("TOTAL", total))
	
def main():
	
  cadProdutos = []

  cadProdutos = f_cadastrarProdutos(cadProdutos)

  cadProdutos = f_venderProdutos(cadProdutos)

  f_imprimirRelVendas(cadProdutos)

#fim
if __name__ == '__main__':
    main()
