# -*- coding: UTF-8 -*-
nomes=[]

def menu():
	print '\n 1 - Cadastrar \n 2 - Remover \n 3 - Listar \n 4 - Alterar \n 0 - Sair \n'
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
	if(op=='4'):
		alterar()
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

def alterar():
	listar()
	print 'Que nome deseja alterar?'
	x=raw_input()
	verifica=x in nomes
	
	if(verifica==True):
		print 'Digite o novo nome:'
		nome_alterado=raw_input()
		nomes[nomes.index(x)]=nome_alterado	
		print 'Nome alterado com sucesso'
		listar()

menu()
