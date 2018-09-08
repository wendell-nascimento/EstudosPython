nomes=[]

def menu():
	print '\n 1 - Cadastrar \n 2 - Remover \n 3 - Listar \n 0 - Sair \n'
	print 'Digite sua escolha: '
	op=raw_input()
	
	
	if(op=='1'):
		cadastrar()
		menu()
	if(op=='2'):
		remover()
		menu()
	if(op=='3'):
		listar()
		menu()

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

def listar():
	print 'Usuarios cadastrados ate o momento: '
	print nomes

menu()
