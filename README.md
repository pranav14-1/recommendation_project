# 🎬 Movie Recommender System

This is my **first machine learning project**, where I built a **content-based movie recommendation system** using Python and integrated it with a **Streamlit web app**.

---

## 🧠 Project Summary

The goal of this project is to recommend similar movies based on their content (genre, cast, overview, etc.). When a user selects a movie from the dropdown, the app displays:

- 🎥 Movie details (fetched from the OMDb API)
- 🧠 Top similar movie recommendations with posters
- 🖱️ Clickable movie posters that lead to new recommendations

The core recommendation logic uses **text-based similarity**, trained and tested in **Jupyter Notebook**, then deployed with a minimal **Streamlit UI**.

---

## 🛠️ Tech Stack
| Layer             | Tech Used                            | Purpose                                              |
|------------------|--------------------------------------|------------------------------------------------------|
| 🧠 Machine Learning | `pandas`, `scikit-learn`, `pickle`    | Data preprocessing, vectorization, cosine similarity |
| 📒 Notebook       | `Jupyter Notebook`                   | Model training and experimentation                   |
| 🌐 Frontend       | `Streamlit`                          | User interface (web app)                             |
| 🌍 APIs           | [OMDb API](https://www.omdbapi.com/) | Fetch real-time movie info like plot, rating, poster |

---

## 🧪 ML Workflow

Here’s a quick breakdown of the ML development process:

1. ✅ Collected movie data from **TMDB**
2. 🧹 Preprocessed the data (cleaned text, selected relevant features)
3. 🧰 Used **Bag of Words (BoW)** via `CountVectorizer` for vectorization
4. 📐 Calculated similarity scores using **cosine similarity**
5. 💾 Saved the final model using `pickle`
6. 🌐 Integrated the model into a **Streamlit app** for easy usage

> 🔬 All model development was done inside **Jupyter Notebook**, and the trained data was exported for deployment.

---

## 🚀 Features

✅ Dropdown-based movie selection  
✅ Full movie info: plot, ratings, genre, director, cast  
✅ Poster image display  
✅ 10 clickable, poster-based movie recommendations  
✅ “Back to Home” navigation  
✅ Simple and interactive Streamlit interface  
✅ API key protected via `.env`

---

## 📈 Future Improvements

Here’s what I plan to do next:

- 📱 Build a fully functional **Flutter mobile app**
- 📺 Add **video streaming feature**:
  - Embed **YouTube trailers** for selected movies
  - Integrate OTT links (Netflix, Prime, etc.)
- 💬 Enable **user reviews and ratings**
- 🧠 Add **collaborative filtering** and **hybrid models**
- 📊 Add filters like genre, year, language, etc.

---
