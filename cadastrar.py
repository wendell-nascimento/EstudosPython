nomes=[]
def cadastrar():
	print 'Digite um nome: '
	nome=raw_input()
	nomes.append(nome)

def remover():
	print nomes
	print 'Que nome deseja remover?'
	nome=raw_input()
	nomes.remove(nome)
	print 'Resultado: '
	print nomes
