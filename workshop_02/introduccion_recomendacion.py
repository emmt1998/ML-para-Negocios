import pandas as pd

peliculas = pd.read_csv("movies.csv")
peliculas.columns = ["peliculaId", "titulo", "generos"]
peliculas = peliculas.set_index("peliculaId")
peliculas.head()

notas = pd.read_csv("ratings.csv")
notas.columns = ["usuarioId", "peliculaId", "nota", "momento"]
notas.head()

notas.describe()

"""# Primera tentativa de recomendacion"""

total_de_votos = notas["peliculaId"].value_counts()
total_de_votos.head()

peliculas['total_de_votos'] = total_de_votos
peliculas.head()

peliculas.sort_values("total_de_votos", ascending = False).head()