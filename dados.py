import csv

def carregar_acessos():

	X = []#X o que eu sei
	Y = []#Y o que quero saber

	arquivo = open('acesso.csv','r')
	leitor = csv.reader(arquivo)

	next(leitor)#nao pega a primeira linha que tem nomes

	for home,como_funciona,contato,comprou in leitor:

		dados = [int(home),int(como_funciona),int(contato)]
		marcacoes = int(comprou)

		X.append(dados)
		Y.append(marcacoes)

	return X, Y


def carregar_buscas():

	X = []
	Y = []

	arquivo = open('buscas.csv','r')#abre arquivo csv no modo 'r' read
	leitor = csv.reader(arquivo)#le modo csv

	next(leitor)#pula primeira linha

	for home,busca,logado,comprou in leitor:
		dados = [int(home), busca, int(logado)]
		X.append(dados)
		Y.append(int(comprou))

	return X, Y