import pandas as pd
from collections import Counter

data_frame = pd.read_csv('buscas_generica.csv')
X_df = data_frame[['home', 'busca', 'logado']]
Y_df = data_frame['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

#X_df.values devolve array com valores

X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_treino = 0.9

tamanho_de_treino = int(porcentagem_treino * len(Y))#90% treino

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

tamanho_de_teste = len(Y) - tamanho_de_treino#restante para treino

teste_dados = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]



from sklearn.naive_bayes import MultinomialNB


modelo = MultinomialNB()

modelo.fit(treino_dados,treino_marcacoes)

resultado = modelo.predict(teste_dados)
acertos = (resultado == teste_marcacoes)

total_de_acertos = sum(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos/total_de_elementos
print(f"Taxa de acertos: {taxa_de_acerto}%")
print(f"Total de elementos:{total_de_elementos}")




acerto_base = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = 100.0 *  acerto_base / len(teste_marcacoes)
print(f"Taxa de acerto base:{taxa_de_acerto_base}")
