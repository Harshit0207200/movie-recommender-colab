# 🎬 Movie Recommender System (Colab + Flask + TMDB API)

A content-based movie recommender built in a Jupyter Notebook using Pandas, cosine similarity, and Flask for UI. Designed for easy deployment inside Google Colab using `flask-ngrok`.

## 📌 Highlights

- Recommends 5 similar movies based on metadata.
- Uses cosine similarity and TMDB API for posters.
- Runs in Colab with Flask using ngrok.

## 📁 Key Files

| File | Description |
|------|-------------|
| `movie_recommender_colab.ipynb` | 🔧 Main notebook – builds model and runs the app |
| `app.py` | 🎯 Flask app (reads `.pkl` files and shows recommendations) |
| `movie_list.pkl` | 📦 Generated DataFrame with movie info |
| `similarity.pkl` | 📦 Cosine similarity matrix |
| `requirements.txt` | 📦 Python dependencies |
| `Screenshot-*.png` | 🖼️ UI visuals |

## ▶️ Run in Google Colab

1. Run all cells in `movie_recommender_colab.ipynb` to generate the `.pkl` files.
2. Start the Flask app using:
    ```python
    !python app.py
    ```
3. Follow the ngrok link to access the web app.

## 🔐 TMDB API

Uses [TMDB API](https://www.themoviedb.org/documentation/api) to fetch movie posters. Replace the API key in `app.py` with your own.

## 📜 License

MIT License — use it freely with attribution.
