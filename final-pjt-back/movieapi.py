import requests
import json

def load_data():
    api_key = '197d30ec014665d8dadc30f98d7007b6'
    start_url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR'
    genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=ko-KR&page=1'
    start_info = requests.get(start_url).json()['total_pages']
    genre_info = requests.get(genre_url).json()['genres']
    movies = []

    for page in range(1, 11):
        print(page)
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page={page}'
        movies_info = requests.get(url).json()['results']
    
        for movie_info in movies_info:
            movie = {}
            movie["model"] = "movies.movie"
            movie["fields"] = {}
            movie["fields"]['title'] = movie_info.get('title')
            movie["fields"]['overview'] = movie_info.get('overview')
            movie["fields"]['release_date'] = movie_info.get('release_date')
            movie["fields"]['poster_path'] = movie_info.get('poster_path')
            movie["fields"]['vote_average'] = movie_info.get('vote_average')
            movie["fields"]['popularity'] = movie_info.get('popularity')
            genres = movie_info.get('genre_ids')
            genre_name = []
            for info in genre_info:
                if info['id'] in genres:
                    genre_name.append(info['name'])
            movie["fields"]['genres'] = genre_name
            movies.append(movie)

    with open('./movies/fixtures/movies.json', 'w', encoding="utf-8") as make_file:
        json.dump(movies, make_file, ensure_ascii=False, indent="\t") 
    print('영화 받아오기 및 저장완료')

load_data()