# Movie_recommender_ML
Content Based Movie Reccomendation system using Cosine similarity. 

Dataset is downloaded from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

To use the following code create environment in the root directory
```
conda create -p venv python==3.9 -y
```
then activate the environement
```
conda activate venv
```
install the dependencies 
```
pip install -r requirements.txt
```
To run the app of local system
```
streamlit run app.py
```
To get the movies poster you need tmdb apikey and movie_id send get request
[READ TMDB API](https://developers.themoviedb.org/3/movies/get-movie-details)

