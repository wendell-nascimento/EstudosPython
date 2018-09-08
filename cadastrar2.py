def cadastrar2():
	print 'Digite o seu ano de nascimento'
	anoAtual=2018
	ano=raw_input()
	ano_inteiro=int(ano)
	idade=anoAtual-ano_inteiro
	return idade
