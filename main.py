import requests
import json
import random


def gather_data():
    apikey = '###'  #Add your API key here
    genre_full_list = [28, 12, 16, 35, 80, 99, 10751, 14, 36, 27, 9648, 878, 10752]
    url = 'https://api.themoviedb.org/3/discover/movie?'

    page_number = random.randint(1, 3)
    year = random.randint(2015, 2020)
    vote = random.randint(6, 8)
    g1 = random.choice(genre_full_list)
    g2 = random.choice(genre_full_list)
    g3 = random.choice(genre_full_list)
    genre = [g1, g2, g3]

    query = {
        'api_key': apikey,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'include_adult': False,
        'page': page_number,
        'primary_release_date.gte': year,
        'vote_average': vote,
        'with_genres': genre,
    }
    try:
        response = requests.get(url, params=query)
        return response
    except Exception:
        return ("COULDN'T CONNECT TO THE DATABASE")


def read_date(response):
    try:
        if response.status_code != 200:
            print("COULDN'T FETCH ANY RESULT")

        else:
            data = json.loads(response.text)
            data = data['results']

            for movies in data:
                print('==========================')
                print('Title ==> ', movies['title'])
                print('Popularity ==> ', movies['popularity'])
                print('Ratings ==> ', movies['vote_average'])
                print('Release date ==> ', movies['release_date'])
                print('Overview ==> ', movies['overview'])

    except Exception:
        print(response)


read_date(gather_data())
