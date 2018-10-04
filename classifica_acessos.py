from dados import carregar_acessos
X, Y = carregar_acessos()

treino_dados = X[:90]#primeiras 90 linhas
treino_marcacoes = Y[:90]

teste_dados = X[-9:]#ultimas 9 linhas
teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB

#Terina
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)


#Prediz
resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos/total_de_elementos
print(f"Taxa de acertos: {taxa_de_acerto}%")