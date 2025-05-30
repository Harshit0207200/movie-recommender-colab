
from flask import Flask, request, render_template_string
import pickle
import requests
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

movies = pickle.load(open("/content/movie_list.pkl", "rb"))
similarity = pickle.load(open("/content/similarity.pkl", "rb"))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return ""

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster = fetch_poster(movie_id)
        recommended_movies.append({'title': title, 'poster': poster})
    return recommended_movies

template = """<!doctype html>
<html>
<head><title>Movie Recommender</title></head>
<body>
<h1>Movie Recommender System</h1>
<form method="post">
    <select name="movie">
    {% for m in movie_list %}
        <option value="{{m}}">{{m}}</option>
    {% endfor %}
    </select>
    <input type="submit" value="Recommend">
</form>
<div>
{% for rec in recommendations %}
    <div style="display:inline-block;margin:10px;text-align:center;">
        <img src="{{rec.poster}}" width="150"><br>
        {{rec.title}}
    </div>
{% endfor %}
</div>
</body>
</html>"""


@app.route('/', methods=['GET', 'POST'])
def home():
    movie_list = movies['title'].values
    recommendations = []
    if request.method == 'POST':
        selected_movie = request.form['movie']
        recommendations = recommend(selected_movie)
    return render_template_string(template, movie_list=movie_list, recommendations=recommendations)

app.run()
