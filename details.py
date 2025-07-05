import requests

TMDB_API_KEY = "your_tmdb_api_key"

def fetch_movie_details(movie_title):
    search_url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": 10d0c287a97f7487bffb955d223fd196,
        "query": movie_title
    }
    response = requests.get(search_url, params=params)
    data = response.json()
    if data['results']:
        movie = data['results'][0]
        return {
            "title": movie['title'],
            "overview": movie['overview'],
            "poster_path": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
            "rating": movie['vote_average'],
            "release_date": movie['release_date']
        }
    return None
