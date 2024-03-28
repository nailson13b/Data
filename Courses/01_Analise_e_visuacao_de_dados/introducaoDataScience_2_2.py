import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


notas = pd.read_csv(r"ml-latest-small\ratings.csv")
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
filmes = pd.read_csv(r"ml-latest-small\movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]

# # print(filmes.head())
# print(notas.query("filmeId==1").nota.mean())
medias_por_filme = notas.groupby("filmeId").mean()["nota"]
print(medias_por_filme.head())

# plt.hist(medias_por_filme)
# # plt.title("Histograma das medias dos filmes")
# plt.show()

print(medias_por_filme.describe())


plt.figure(figsize=(5,8))
sns.boxplot(medias_por_filme)
plt.show()

# sns.distplot(medias_por_filme)
# plt.show()