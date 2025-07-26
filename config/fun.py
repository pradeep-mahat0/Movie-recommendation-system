import requests
import os
import pickle

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raises HTTPError if status is 4xx or 5xx
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster"
    except Exception as e:
        print(f"[ERROR] API request failed for movie_id={movie_id} -> {e}")
        return "https://via.placeholder.com/500x750.png?text=Error"
    

# def fetch_poster(movie_id):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
#         response = requests.get(url, timeout=(3,5))
#         response.raise_for_status()  # raises HTTPError for bad responses (4xx/5xx)

#         data = response.json()
#         poster_path = data.get('poster_path')

#         if not poster_path:
#             raise ValueError("Poster path not found in response")

#         full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
#         return full_path

#     except requests.exceptions.RequestException as e:
#         print(f"[ERROR] API request failed for movie_id={movie_id} -> {e}")
#     except ValueError as e:
#         print(f"[WARNING] No poster found for movie_id={movie_id}")
#     except Exception as e:
#         print(f"[FATAL] Unexpected error for movie_id={movie_id} -> {e}")

#     # Return a fallback image in case of any failure
#     return "https://via.placeholder.com/500x750?text=Image+Unavailable"


def recommend(movie):
    index = movies[movies['title_x'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title_x)

    return recommended_movie_names,recommended_movie_posters