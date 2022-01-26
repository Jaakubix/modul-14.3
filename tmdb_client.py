import requests, random
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjdlNjM2NTk4MDgzNzZlY2FkM2Y2MmUxMjY1ZDhlZSIsInN1YiI6IjYxZGMzYTdkZTE5ZGU5MDA4ZDE1NmZiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DNuTut1HT8rcJZNzcIRNCejk9DpqAWpVRzH58kHnPO8"

def get_popular_movies(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
    
def get_movies(how_many, list_type):
    data = get_popular_movies(list_type)['results']
    return random.sample(data, k=len(data))[:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()\

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_genres():
    endpoint = "https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response = response.json()['genres']
    return response

def list_type_check(list_type):
    genres = get_genres()
    genres = [genres['name'] for genres in genres]
    for genre in genres:
        if list_type == genre:
            return True
        else:
            get_movies(how_many=8, list_type="popular")
    return genres