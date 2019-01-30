import fresh_tomatoes
import media
import yaml
import tmdbsimple as tmdb

BASE_URL_POSTER = "https://image.tmdb.org/t/p/w500"

BASE_URL_YOUTUBE_TRAILER = "https://www.youtube.com/watch?v="

def get_movies_from_file():
    # Obtem a lista de filmes a partir de arquivo no formato yaml
    movies_list_doc = open("./movies_list.yaml")
    # Carrega e efetua o parse com os dados do arquivo no formato da classe Movie
    parsed_movies = yaml.load(movies_list_doc)
    return parsed_movies

def get_id_youtube_trailer(movie_id):
	return tmdb.Movies(movie_id).videos()['results'][0]['key']

def create_movie_from(r_dict):
    movie_id = r_dict['id']
    movie_title = r_dict['title']
    movie_storyline = r_dict['overview']
    poster_path = BASE_URL_POSTER + r_dict['poster_path'] 
    youtube_trailer = BASE_URL_YOUTUBE_TRAILER + get_id_youtube_trailer(movie_id)
    
    return media.Movie(movie_title, movie_storyline, poster_path, youtube_trailer)

def get_movies_from_tmdb():
    # tmdb.API_KEY = '<MY_API_KEY>'
    client = tmdb.Movies()

    movies_upcoming_dict = client.upcoming()

    movies = []
    for r_dict in movies_upcoming_dict['results']:
        movies.append(create_movie_from(r_dict))

    return movies

movies = []
try:
    movies = get_movies_from_tmdb()
except:
    movies = get_movies_from_file()

print len(movies)

fresh_tomatoes.open_movies_page(movies)
