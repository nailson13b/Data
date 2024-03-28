import pandas as pd
import matplotlib.pyplot as mpl
import seaborn as sns

notas = pd.read_csv(r"ml-latest-small\ratings.csv")
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
print(notas.nota.head())
# mpl.hist(notas.nota)
# mpl.show()
print("Media" ,notas.nota.mean())
print("Mediana" ,notas.nota.median())
print(notas.nota.describe())

sns.boxplot(notas.nota)
mpl.show()