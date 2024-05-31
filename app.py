import streamlit as st
import pickle
import requests

# Function to fetch movie details
def fetch_movie_details(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return data

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_details = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_details = fetch_movie_details(movie_id)
        recommended_movie_details.append(movie_details)

    return recommended_movie_details

# Custom CSS
custom_css = """
<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    padding: 20px;
}

.title {
    font-size: 50px;
    color: #333333;
    margin-bottom: 20px;
}

.sub-title {
    font-size: 36px;
    color: #666666;
    margin-bottom: 10px;
}

.movie-container {
    background-color: #ffffff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.movie-title {
    font-size: 18px;
    color: #333333;
    margin-bottom: 10px;
}

.movie-details {
    font-size: 14px;
    color: #666666;
}

</style>
"""


st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")

st.markdown(custom_css, unsafe_allow_html=True)

st.title("Movie Recommendation System")

movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown list", movie_list)

if st.button("Show Recommendations"):
    st.markdown("## Recommendations")
    recommended_movies = recommend(selected_movie)
    
    cols = st.columns(5)  
    for movie, col in zip(recommended_movies, cols):
        with col:
            st.markdown('<div class="movie-container"><img src="{}" width="150"><div class="movie-title">{}</div><div class="movie-details">Release Date: {}<br>Vote Average: {}</div></div>'.format(fetch_poster(movie['id']), movie['title'], movie['release_date'], movie['vote_average']), unsafe_allow_html=True)
