import fresh_tomatoes
import media
import yaml

movies_list_doc = open("./movies_list.yaml")

parsed_movies = yaml.load(movies_list_doc)

movies = []
for movie in parsed_movies:
	movies.append(movie)

fresh_tomatoes.open_movies_page(movies)