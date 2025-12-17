# 🎵 Song Recommendation System (FastAPI)

A content-based song recommendation system built using **TF-IDF** and **cosine similarity**.  
The system recommends similar songs based on lyrics and metadata, and exposes the model through a **FastAPI REST API**.

## 📌 Project Overview

This project implements a **content-based music recommendation system**.
Instead of using user ratings, it analyzes **song lyrics and metadata** to find similar songs.

The recommendation process follows this workflow:

1. Text preprocessing of song data
2. Feature extraction using TF-IDF
3. Similarity computation using cosine similarity
4. Recommendation served through a FastAPI backend

## ✨ Features

- Content-based song recommendation system
- Uses **TF-IDF Vectorization** on song lyrics and metadata
- Computes similarity using **Cosine Similarity**
- Handles spelling mistakes using **difflib**
- Built with **FastAPI** for easy API access
- REST API tested using **Swagger UI** and **Postman**

## 🧠 How It Works (Simple Flow)

1. Load and clean song dataset
2. Combine song features (artist, title, lyrics)
3. Apply TF-IDF vectorization
4. User provides a song name
5. System finds the closest matching song
6. Cosine similarity is calculated
7. Top similar songs are returned as recommendations

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **scikit-learn**
- **pandas**
- **Uvicorn**
- **Postman**
- **Git & GitHub**

# ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
git clone https://github.com/christyabhi/song-recommendation-fastapi.git
cd song-recommendation-fastapi

### 2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the FastAPI server
uvicorn main:app --reload

🌐 API Endpoints
# Root Endpoint
GET /

Response:

{
  "message": "Song Recommendation API"
}

# Recommendation Endpoint
POST /recommendation

Request Body:

{
  "song": "Hello"
}


Response:

{
  "matched_song": "Hello",
  "recommendations": [
    "Hello - Adele",
    "Hello Again - Neil Diamond",
    "Hello Love - Hank Snow"
  ]
}



# 🧪 API Testing

Swagger UI:
👉 http://127.0.0.1:8000/docs

Postman:
Use POST request with JSON body



# 📌 Notes

This is a content-based recommender

Recommendations are based on text similarity, not popularity

Large dataset (~57k songs) handled efficiently



# 👨‍💻 Author
ABHISHEK (christyabhi)
Electrical and electronic engineer | AI Enthusiast | Beginner Data Analyst 🚀



# ⭐ Acknowledgements

DevTown Bootcamp

scikit-learn documentation

FastAPI documentation