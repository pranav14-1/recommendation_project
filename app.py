import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# Load movie data
movies_list = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_df = pd.DataFrame(movies_list)

# --- Helper Functions ---
def fetch_movie_details(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "False":
            return None
        return {
            "title": data.get("Title", "N/A"),
            "year": data.get("Year", "N/A"),
            "rating": data.get("imdbRating", "N/A"),
            "plot": data.get("Plot", "No description."),
            "poster": data.get("Poster", ""),
            "genre": data.get("Genre", "N/A"),
            "director": data.get("Director", "N/A"),
            "actors": data.get("Actors", "N/A"),
            "box_office": data.get("BoxOffice", "N/A"),
            "ratings": data.get("Ratings", [])
        }
    except:
        return None

def recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:11]
    return [movies_df.iloc[i[0]].title for i in movie_indices]

# --- Streamlit App ---
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Smart Movie Recommender")

# Query param
query_params = st.query_params
selected_movie = query_params.get("movie", None)

# --- Dropdown UI ---
st.markdown("### 🎞️ Select a Movie to Get Started")

selected = st.selectbox(
    "Select from the list",
    movies_df['title'].values,
    index=None,
    placeholder="Choose a movie..."
)

if st.button("🎯 Search", disabled=selected is None):
    st.query_params["movie"] = selected
    st.rerun()

# --- Home screen before selection ---
if not selected_movie:
    st.info("⬆️ Select a movie and click 'Recommend' to begin.")
    st.stop()

# --- Movie Detail Section ---
details = fetch_movie_details(selected_movie)
if details:
    st.markdown("### 🎥 Movie Details")
    col1, col2 = st.columns([1, 2])
    with col1:
        if details["poster"] and details["poster"] != "N/A":
            st.image(details["poster"], width=300)
    with col2:
        st.subheader(details["title"])
        st.write(f"**Year:** {details['year']}")
        st.write(f"**IMDb Rating:** ⭐ {details['rating']}")
        st.write(f"**Genre:** {details['genre']}")
        st.write(f"**Director:** {details['director']}")
        st.write(f"**Actors:** {details['actors']}")
        st.write(f"**Box Office:** {details['box_office']}")
        st.markdown(f"**Plot:** {details['plot']}")
        for r in details["ratings"]:
            st.write(f"• {r['Source']}: {r['Value']}")

    if st.button("⬅️ Back to Home"):
        st.query_params.clear()
        st.rerun()

    # --- Recommendations ---
    st.markdown("---")
    st.subheader("🎯 Recommended Movies")

    recommendations = recommend(details["title"])
    rec_cols = st.columns(len(recommendations))

    for idx, movie in enumerate(recommendations):
        rec_details = fetch_movie_details(movie)
        if rec_details and rec_details["poster"] and rec_details["poster"] != "N/A":
            with rec_cols[idx]:
                st.markdown(
                    f"""
                    <a href="?movie={movie}" style="text-decoration: none;">
                        <img src="{rec_details['poster']}" width="150"/><br>
                        <center><b style="color: white;">{movie}</b></center>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
else:
    st.warning("⚠️ Movie not found or OMDb request failed.")
