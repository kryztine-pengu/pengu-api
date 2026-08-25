from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Simple Movie API",
    description="A beginner-friendly REST API containing information about movies.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MOVIE DATA
movies = [

    {
        "id": 1,
        "title": "Spider-Man",
        "year": 2002,
        "genre": "Action, Superhero",
        "director": "Sam Raimi",
        "rating": 7.4,
        "description": "A teenager gains spider-like abilities and learns to use them to become a hero."
    },

    {
        "id": 2,
        "title": "Insidious",
        "year": 2010,
        "genre": "Horror, Mystery",
        "director": "James Wan",
        "rating": 6.8,
        "description": "A family discovers that their son is trapped in a mysterious supernatural realm."
    },

    {
        "id": 3,
        "title": "Frozen",
        "year": 2013,
        "genre": "Animation, Adventure, Fantasy",
        "director": "Chris Buck and Jennifer Lee",
        "rating": 7.4,
        "description": "A fearless princess sets out to find her sister and save their kingdom from an eternal winter."
    },

    {
        "id": 4,
        "title": "Tangled",
        "year": 2010,
        "genre": "Animation, Adventure, Comedy",
        "director": "Nathan Greno and Byron Howard",
        "rating": 7.7,
        "description": "A young princess with magical long hair escapes her tower and discovers the world outside."
    },

    {
        "id": 5,
        "title": "Interstellar",
        "year": 2014,
        "genre": "Aventure, Drama, Sci-Fi",
        "director": "Christopher Nolan",
        "rating": 8.7,
        "description": "In a dystopian future where Earth has become near-uninhabitable, a team of astronauts embark on a mission to find a new home for humanity.",
    },

    {
        "id": 6,
        "title": "Inception",
        "year": 2010,
        "genre": "Adventure, Sci-Fi, Thriller",
        "director": "Nathan Greno and Byron Howard",
        "rating": 7.7,
        "description": "A young princess with magical long hair escapes her tower and discovers the world outside."
    }
]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Simple Movie API!",
        "endpoints": [
            "/movies",
            "/movies/{id}",
            "/movies/search"
        ]
    }


# GET ALL MOVIES
@app.get("/movies")
def get_movies():

    return {
        "count": len(movies),
        "movies": movies
    }


# SEARCH MOVIES
@app.get("/movies/search")
def search_movies(q: str = Query(..., min_length=1)):

    q = q.lower()
    results = []

    for movie in movies:

        searchable_text = (
            f"{movie['title']} "
            f"{movie['year']} "
            f"{movie['genre']} "
            f"{movie['director']}"
        ).lower()

        if q in searchable_text:
            results.append(movie)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }


# GET ONE MOVIE
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):

    for movie in movies:

        if movie["id"] == movie_id:
            return movie

    raise HTTPException(
        status_code=404,
        detail="Movie not found."
    )
