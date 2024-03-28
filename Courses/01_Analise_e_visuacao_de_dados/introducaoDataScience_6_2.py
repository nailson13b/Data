import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tmdb = pd.read_csv(r"archive\tmdb_5000_movies.csv")

notas = pd.read_csv(r"ml-latest-small\ratings.csv")
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
filmes = pd.read_csv(r"ml-latest-small\movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]


print(filmes.head(2))

notas_do_toy_story = notas.query("filmeId==1")
notas_do_jumanji = notas.query("filmeId==2")
print(len(notas_do_toy_story), len(notas_do_jumanji))

print("Nota media do Toy Story %.2f" %notas_do_toy_story["nota"].mean())
print("Nota media do Jumanji %.2f" %notas_do_jumanji["nota"].mean())

print("Nota mediana do Toy Story %.2f" %notas_do_toy_story["nota"].median())
print("Nota mediana do Jumanji %.2f" %notas_do_jumanji["nota"].median())

print(np.array([2.5] * 10))
print(np.array([3.5] * 10))

filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
filme2 = np.append(np.array([5] * 10), np.array([1] * 10))

print(filme1.mean(), filme2.mean())
print(np.std(filme1), np.std(filme2))
print(np.median(filme1), np.median(filme2))

# plt.hist(filme1)
# plt.hist(filme2)
# plt.show()

# plt.boxplot([filme1, filme2])
# plt.show()

# plt.boxplot([notas_do_toy_story["nota"], notas_do_jumanji["nota"]])
# plt.show()

# sns.boxplot(x = "filmeId", y="nota", data = notas)
# plt.show()

sns.boxplot(x = "filmeId", y="nota", data = notas.query("filmeId in [1,2]"))
plt.show()

