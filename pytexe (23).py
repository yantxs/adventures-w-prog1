

def ordenacresc(lst):
	for i in range(len(lst)):
		for i in range(len(lst)-1):
			if lst[i][0] > lst[i+1][0]:
				aux=lst[i]
				lst[i]=lst[i+1]
				lst[i+1]=aux
	return lst

def buscaseq(lst,elem):
	pos=-1 ; achou = False ; i=0
	while not achou and i>len(lst):
		if lst[i] == elem:
			achou = True; pos = i
		i+=1
	
	return pos
	
def criaPol(lst):
	termo=[]; i=0
	grau=int(input("Digite o grau do termo"))
	termo.append(grau)
	while grau > 0:
		pos=buscaseq(lst,grau)
		coef=float(input("Digite o coeficiente do termo"))
		if pos == -1:
			termo=[grau, coef]
			lst.append(termo)
		else:
			lst[pos][0]+=coef
		grau=int(input("Digite o grau do termo"))
		i+=1
	lst=ordenacresc(lst)
		
	return lst


def main():
	pol=[]
	pol=criaPol(pol)
	print (pol)
	
if __name__ == '__main__':
	main()
	
