# Import the Libraries
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import difflib

app = FastAPI()             # Initializing my app as FastAPI
app.add_middleware(
    CORSMiddleware,         # Anyone can access the API from anywhere
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

songs_data = pd.read_csv("spotify_millsongdata.csv")

selected_features = ['artist', 'song', 'text']

for feature in selected_features:
    songs_data[feature] = songs_data[feature].fillna('')

combined_features = songs_data['artist']+' ' + \
    songs_data['song']+' '+songs_data['text']

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

list_of_all_songs = songs_data['song'].tolist()

# maintain user input as Class


class SongRequest(BaseModel):
    song: str

# create End Point where user can hit and access all the things


@app.get("/")
def root():
    # this is the message user will see while accessing API
    return {"message": "Song Recommendation API"}


# create the next End Point
@app.post("/recommendation")
def recommend(request: SongRequest):
    song_name = request.song
    find_close_match = difflib.get_close_matches(song_name, list_of_all_songs)

    if not find_close_match:
        return {"error": "No matching song found"}

    close_match = find_close_match[0]

    index_of_the_song = songs_data[songs_data.song == close_match].index[0]

    similarity_scores = cosine_similarity(
        feature_vectors[index_of_the_song],
        feature_vectors
    )

    similarity_score_list = list(enumerate(similarity_scores[0]))

    sorted_similar_songs = sorted(
        similarity_score_list,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []
    i = 1

    for song in sorted_similar_songs[1:11]:
        index = song[0]
        title = songs_data.iloc[index]['song']
        artist = songs_data.iloc[index]['artist']
        recommendations.append(f"{title} - {artist}")

    return {
        "matched_songs": close_match,
        "recommendations": recommendations
    }
