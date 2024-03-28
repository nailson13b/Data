import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tmdb = pd.read_csv(r"archive\tmdb_5000_movies.csv")

print(tmdb.head())

print(tmdb.original_language.unique())

print(tmdb["original_language"].value_counts().index)

print(tmdb["original_language"].value_counts().values)

contagem_de_lingua = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ["original_language", "total"]
print(contagem_de_lingua.head())

# sns.barplot(x="original_language", y="total", data = contagem_de_lingua)
# plt.show()

# sns.catplot(x="original_language", kind="count", data=tmdb)
# plt.show()

# plt.pie(contagem_de_lingua["total"], labels=contagem_de_lingua["original_language"])
# plt.show()

total_por_lingua = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles
# print(total_de_ingles, total_do_resto)

dados = {
    'lingua' : ['ingles', 'outros'],
    'total' : [total_de_ingles, total_do_resto]
}

pd.DataFrame(dados)

# custom_colors = ["blue", "orange"]
# sns.barplot(x="lingua", y="total", palette= custom_colors, data= dados)
# plt.show()

total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'")["original_language"].value_counts()
filmes_sem_lingua_em_ingles = tmdb.query("original_language != 'en'")


sns.catplot(x="original_language", kind="count", data=filmes_sem_lingua_em_ingles, aspect=2, palette="mako", order=total_por_lingua_de_outros_filmes.index)
plt.show()
