import fresh_tomatoes
import media
import yaml
import tmdbsimple as tmdb

BASE_URL_POSTER = "https://image.tmdb.org/t/p/w500"

BASE_URL_YOUTUBE = "https://www.youtube.com/watch?v="


def get_movies_from_file():
    """Retorna uma lista de filmes.

    Recupera um conjunto de filmes (no formato media.Movie) a partir de
    um arquivo yaml.
    """

    # Obtem a lista de filmes a partir de arquivo no formato yaml
    movies_list_doc = open("./movies_list.yaml")
    # Le os dados do arquivo e instancia objetos da classe Movie
    parsed_movies = yaml.load(movies_list_doc)
    movies_list_doc.close()
    return parsed_movies


def get_id_youtube_trailer(movie_id):
    """Devolve o id do trailer no Youtube.

    Recupera o identificador do trailer no youtube a partir da API do TMDB
    com base no identificador do filme informado.

    Args:
        movie_id: Id do filme no tmdb.
    """

    return tmdb.Movies(movie_id).videos()['results'][0]['key']


def create_movie_from(r_dict):
    """Cria e devolve uma instancia de media.Movie.

    Instancia um objeto Movie a partir de um objeto dict contendo
    as propriedades do filme.

    Args:
        r_dict: Dicionario chave-valor contendo os dados do filme.
    """

    movie_id = r_dict['id']
    title = r_dict['title']
    storyline = r_dict['overview']
    poster_path = BASE_URL_POSTER + r_dict['poster_path']
    youtube_trailer = BASE_URL_YOUTUBE + get_id_youtube_trailer(movie_id)

    return media.Movie(title, storyline, poster_path, youtube_trailer)


def get_movies_from_tmdb():
    """Retorna uma lista de filmes.

    Utiliza a API do https://www.themoviedb.org para recuperar um conjunto
    de filmes.
    """

    # Substituir o <MY_API_KEY> pela chave utilizada para acesso a API do tmdb.
    tmdb.API_KEY = '<MY_API_KEY>'
    client = tmdb.Movies()

    # A function upcoming() devolve os filmes mais recentes.
    movies_upcoming_dict = client.upcoming()

    movies = []
    for r_dict in movies_upcoming_dict['results']:
        movies.append(create_movie_from(r_dict))

    return movies

# Execute script
movies = []
try:
    movies = get_movies_from_tmdb()
except:
    movies = get_movies_from_file()

print len(movies)

fresh_tomatoes.open_movies_page(movies)
