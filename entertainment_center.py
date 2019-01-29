import fresh_tomatoes
import media
import yaml

# Obtem a lista de filmes a partir de arquivo no formato yaml
movies_list_doc = open("./movies_list.yaml")

# Carrega e efetua o parse com os dados do arquivo ja no formato da classe Movie
parsed_movies = yaml.load(movies_list_doc)

movies = []
for movie in parsed_movies:
	movies.append(movie)

fresh_tomatoes.open_movies_page(movies)