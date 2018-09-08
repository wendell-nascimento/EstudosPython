def gera_nome_convite(nome):
	tamanho=len(nome)
	parte1=nome[0:4]
	parte2=nome[tamanho-4:tamanho]
	return parte1 + ' '+ parte2

def envia_convite(nome_formatado):
	print 'Enviando convite para %s ' % (nome_formatado)
