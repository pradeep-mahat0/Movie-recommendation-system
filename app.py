import pickle
import streamlit as st
from config.fun import recommend



movies = pickle.load(open('model/movie_list.pkl','rb'))
st.header('Movie Recommender System')


movie_list = movies['title_x'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])