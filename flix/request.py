import urllib.request, json
from .models import Movie

api_key='8b8b8b7eed8c7bb30b5f667020f505ba'

base_url='https://api.themoviedb.org/3/movie/'

def all_movies(category):

    all_movies_url= base_url+'popular?api_key='+api_key+'&language=en-US'

    with urllib.request.urlopen(all_movies_url) as url:
        all_movies_data= url.read().decode('utf-8')

        get_all_movies = json.loads(f'''{all_movies_data}''')


        movie_results = None

        if get_all_movies['results']:
            movie_results = get_all_movies['results']
    return movie_results
