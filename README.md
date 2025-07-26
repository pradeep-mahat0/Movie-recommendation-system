# Movie-recommendation-system


This project is a **content-based movie recommendation system** built using the TMDB 5000 Movie Dataset. It recommends similar movies based on selected features like genres, keywords, cast, and crew.

---

##  Dataset

The dataset is sourced from Kaggle:

- [`tmdb_5000_movies.csv`](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- `tmdb_5000_credits.csv`

These files contain metadata for 5000 movies including genres, keywords, cast, crew, and more.

---

## Features Used

- **Genres**
- **Keywords**
- **Cast**
- **Overview**
- **Director (from crew)**

These features are combined into a single string per movie and vectorized using **TF-IDF** or **CountVectorizer** for computing **cosine similarity**.

---

## Technologies Used

- Python 
- Pandas
- Scikit-learn
- Numpy
- Pickle (for saving the model and similarity matrix)
- Streamlit (optional, for frontend UI)

---

## How It Works

1. **Load the data** using Pandas.
2. **Merge** movies and credits datasets on `movie_id`.
3. Extract relevant fields: genres, keywords, Overview, cast, crew.
4. Preprocess and combine them into a single textual feature (`tags`).
5. Convert text to vectors using **CountVectorizer**.
6. Compute **cosine similarity** between all movie vectors.
7. Use the similarity matrix to return top N similar movies.

---

## Output Files

- `movie_list.pkl`: Pickled list of all movie titles and their metadata.
- `similarity.pkl`: Pickled cosine similarity matrix used for recommendations. this file size is too big for github so i don't upload it.you can get it by running the notebook.
- 




