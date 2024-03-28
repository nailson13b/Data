import pandas as pd


notas = pd.read_csv(r"ml-latest-small\ratings.csv")
print (notas.head())
print (notas.shape)
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
print (notas.head())
print (notas['nota'])
print (notas['nota'].unique())
print (notas['nota'].value_counts())
print (notas['nota'].mean())
