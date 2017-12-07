
def f_imprimirRelVendas(lst):
	total=0.0
	print("{:>8}  |{:>6}".format("PRODUTO","TOTAL VENDIDO"))
	for i in range(len(lst)):
		nome=lst[i][0]; pcompra=lst[i][1]; pvenda=lst[i][2]; vend=lst[i][4];
		totvend=vend*pvenda
		total+=totvend
		if vend != 0:
			print("{:<8}  |R${:>6.2f}".format(nome, totvend))
	print("______________________")
	print("{:^8}  |R${:>6.2f}".format("TOTAL", total))

def main():
	lst=[["Macarrão", 1.00, 2.84, 10, 5],["Arroz", 4.00, 8.67, 20, 27]]
	f_imprimirRelVendas(lst)

if __name__=='__main__':
	main()
