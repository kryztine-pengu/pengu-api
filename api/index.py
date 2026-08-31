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
        "duration": "2h 1m",
        "year": 2002,
        "agelimit": "PG-13",
        "genre": "Action, Superhero",
        "stars": "Tobey Maguire, Kirsten Dunst, Willem Dafoe",
        "director": "Sam Raimi",
        "writers": "Stan Lee, Steve Ditko, David Koepp",
        "streaming": "Netflix",
        "rating": 7.4,
        "userreviews": "2.6k",
        "metascore": 73,
        "popularity": 59,
        "description": "A teenager gains spider-like abilities and learns to use them to become a hero.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Spider-Man"
    },

    {
        "id": 2,
        "title": "Insidious",
        "duration": "1h 43m",
        "year": 2010,
        "agelimit": "PG-13",
        "genre": "Horror, Mystery",
        "stars": "Patrick Wilson, Rose Byrne, Ty Simpkins",
        "director": "James Wan",
        "writers": "Leigh Whannell",
        "streaming": "Netflix",
        "rating": 6.8,
        "userreviews": "1.1k",
        "metascore": 52,
        "popularity": 48,
        "description": "A family discovers that their son is trapped in a mysterious supernatural realm.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Insidious"
    },

    {
        "id": 3,
        "title": "Frozen",
        "duration": "1h 42m",
        "year": 2013,
        "agelimit": "PG",
        "genre": "Animation, Adventure, Fantasy",
        "stars": "Kristen Bell, Idina Menzel, Jonathan Groff",
        "director": "Chris Buck and Jennifer Lee",
        "writers": "Jennifer Lee, Hans Christian Andersen, Chris Buck",
        "streaming": "Disney+",
        "rating": 7.4,
        "userreviews": "1.3k",
        "metascore": 75,
        "popularity": 570,
        "description": "A fearless princess sets out to find her sister and save their kingdom from an eternal winter.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Frozen"
    },

    {
        "id": 4,
        "title": "Tangled",
        "duration": "1h 40m",
        "year": 2010,
        "agelimit": "PG",
        "genre": "Animation, Adventure, Fantasy",
        "stars": "Mandy Moore, Zachary Levi, Donna Murphy",
        "director": "Nathan Greno and Byron Howard",
        "writers": "Dan Fogelman, Jacob Grimm, Wilhelm Grimm",
        "streaming": "Disney+",
        "rating": 8.5,
        "userreviews": 668,
        "metascore": 71,
        "popularity": 636,
        "description": "Rapunzel leaves her tower for the first time and discovers the world outside.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Tangled"
    },

    {
        "id": 5,
        "title": "Interstellar",
        "duration": "2h 49m",
        "year": 2014,
        "agelimit": "PG-13",
        "genre": "Adventure, Sci-Fi",
        "stars": "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        "director": "Christopher Nolan",
        "writers": "Jonathan Nolan, Christopher Nolan",
        "streaming": "Amazon Prime",
        "rating": 8.7,
        "userreviews": "7.4k",
        "metascore": 74,
        "popularity": 36,
        "description": "A team of astronauts travels through space in search of a new home for humanity.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Interstellar"
    },

    {
        "id": 6,
        "title": "The Lord of the Rings: The Two Towers",
        "duration": "2h 59m",
        "year": 2002,
        "agelimit": "PG-13",
        "genre": "Action, Adventure, Sci-Fi",
        "stars": "Elijah Wood, Ian McKellen, Viggo Mortensen",
        "director": "Peter Jackson",
        "writers": "J.R.R. Tolkien, Fran Walsh, Philippa Boyens",
        "streaming": "Netflix",
        "rating": 8.8,
        "userreviews": "2.9k",
        "metascore": 87,
        "popularity": 413,
        "description": "Frodo and Sam continue toward Mordor while the divided fellowship faces new enemies.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Lord+of+the+Rings"
    },

    {
        "id": 7,
        "title": "Forrest Gump",
        "duration": "2h 22m",
        "year": 1994,
        "agelimit": "PG-13",
        "genre": "Romance",
        "stars": "Tom Hanks, Robin Wright, Gary Sinise",
        "director": "Robert Zemeckis",
        "writers": "Winston Groom, Eric Roth",
        "streaming": "HBO",
        "rating": 8.8,
        "userreviews": "3.5k",
        "metascore": 82,
        "popularity": 193,
        "description": "The extraordinary life of an Alabama man unfolds through decades of American history.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Forrest+Gump"
    },

    {
        "id": 8,
        "title": "Inception",
        "duration": "2h 28m",
        "year": 2010,
        "agelimit": "PG-13",
        "genre": "Action, Sci-Fi",
        "stars": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
        "director": "Christopher Nolan",
        "writers": "Christopher Nolan",
        "streaming": "HBO",
        "rating": 8.8,
        "userreviews": "5.2k",
        "metascore": 74,
        "popularity": 61,
        "description": "A thief enters people's dreams to steal secrets and is given a dangerous new mission.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Inception"
    },

    {
        "id": 9,
        "title": "The End of Oak Street",
        "duration": "1h 39m",
        "year": 2026,
        "agelimit": "PG-13",
        "genre": "Action, Sci-Fi",
        "stars": "Anne Hathaway, Ewan McGregor, Maisy Stella",
        "director": "David Robert Mitchell",
        "writers": "David Robert Mitchell",
        "streaming": "In Theaters",
        "rating": 6.6,
        "userreviews": 526,
        "metascore": 69,
        "popularity": 150,
        "description": "The Platt family bands together after a cosmic event transports their neighborhood to an unknown place.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Oak+Street"
    },

    {
        "id": 10,
        "title": "Obsession",
        "duration": "1h 49m",
        "year": 2026,
        "agelimit": "R-18",
        "genre": "Romance, Horror, Thriller",
        "stars": "Michael Johnston, Inde Navarrette, Cooper Tomlinson",
        "director": "Curry Barker",
        "writers": "Curry Barker",
        "streaming": "Online Websites",
        "rating": 7.8,
        "userreviews": "339k",
        "metascore": 77,
        "popularity": 286,
        "description": "After making a mysterious wish to win his crush's heart, a hopeless romantic discovers that some desires come at a sinister price.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Obsession"
    },

    {
        "id": 11,
        "title": "Project Hail Mary",
        "duration": "2h 36m",
        "year": 2026,
        "agelimit": "PG-13",
        "genre": "Adventure, Comedy, Sci-Fi",
        "stars": "Ryan Gosling, Sandra Hüller, James Ortiz",
        "director": "Phil Lord, Christopher Miller",
        "writers": "Drew Goddard, Andy Weir",
        "streaming": "Prime",
        "rating": 8.2,
        "userreviews": "4.5k",
        "metascore": 77,
        "popularity": 600,
        "description": "A science teacher wakes up alone on a spaceship and discovers a mission to save Earth's sun.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Project+Hail+Mary"
    },

    {
        "id": 12,
        "title": "The Devil Wears Prada 2",
        "duration": "1h 59m",
        "year": 2026,
        "agelimit": "PG-13",
        "genre": "Comedy, Drama",
        "stars": "Meryl Streep, Anne Hathaway, Emily Blunt",
        "director": "Phil Lord, Christopher Miller",
        "writers": "Lauren Weisberger, Aline Brosh McKenna",
        "streaming": "Disney+",
        "rating": 6.3,
        "userreviews": "924",
        "metascore": 63,
        "popularity": 28,
        "description": "A fashion magazine editor faces new challenges as her protégé rises in the industry.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Devil+Wears+Prada"
    },

    {
        "id": 13,
        "title": "X-Men",
        "duration": "1h 44m",
        "year": 2000,
        "agelimit": "PG-13",
        "genre": "Action, Adventure, Sci-Fi, Political Drama",
        "stars": "Patrick Stewart, Hugh Jackman, Ian McKellen",
        "director": "Bryan Singer",
        "writers": "Tom DeSanto, Bryan Singer, David Hayter",
        "streaming": "HBO",
        "rating": 7.3,
        "userreviews": "1.6k",
        "metascore": 64,
        "popularity": 49,
        "description": "Mutants face discrimination while two opposing groups clash over humanity's fate.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=X-Men"
    },

    {
        "id": 14,
        "title": "The Matrix",
        "duration": "2h 16m",
        "year": 1999,
        "agelimit": "R",
        "genre": "Action, Sci-Fi",
        "stars": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
        "director": "The Wachowskis",
        "writers": "The Wachowskis",
        "streaming": "HBO",
        "rating": 8.7,
        "userreviews": "6.1k",
        "metascore": 73,
        "popularity": 500,
        "description": "A hacker discovers that reality is a simulation and joins a rebellion against machines.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=The+Matrix"
    },

    {
        "id": 15,
        "title": "Avatar",
        "duration": "2h 42m",
        "year": 2009,
        "agelimit": "PG-13",
        "genre": "Adventure, Sci-Fi",
        "stars": "Sam Worthington, Zoe Saldana, Sigourney Weaver",
        "director": "James Cameron",
        "writers": "James Cameron",
        "streaming": "Disney+",
        "rating": 7.8,
        "userreviews": "8.2k",
        "metascore": 83,
        "popularity": 700,
        "description": "A marine travels to Pandora and becomes torn between duty and his growing connection to the world.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Avatar"
    },

    {
        "id": 16,
        "title": "The Dark Knight",
        "duration": "2h 32m",
        "year": 2008,
        "agelimit": "PG-13",
        "genre": "Action, Superhero",
        "stars": "Christian Bale, Heath Ledger, Aaron Eckhart",
        "director": "Christopher Nolan",
        "writers": "Jonathan Nolan, Christopher Nolan",
        "streaming": "HBO",
        "rating": 9.0,
        "userreviews": "9.5k",
        "metascore": 84,
        "popularity": 850,
        "description": "Batman faces chaos unleashed by the Joker while protecting Gotham City.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=The+Dark+Knight"
    },

    {
        "id": 17,
        "title": "Titanic",
        "duration": "3h 14m",
        "year": 1997,
        "agelimit": "PG-13",
        "genre": "Romance, Drama",
        "stars": "Leonardo DiCaprio, Kate Winslet, Billy Zane",
        "director": "James Cameron",
        "writers": "James Cameron",
        "streaming": "Disney+",
        "rating": 7.9,
        "userreviews": "10.1k",
        "metascore": 75,
        "popularity": 900,
        "description": "A romance blossoms between two passengers aboard the ill-fated Titanic.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Titanic"
    },

    {
        "id": 18,
        "title": "Jurassic Park",
        "duration": "2h 7m",
        "year": 1993,
        "agelimit": "PG-13",
        "genre": "Adventure, Sci-Fi",
        "stars": "Sam Neill, Laura Dern, Jeff Goldblum",
        "director": "Steven Spielberg",
        "writers": "Michael Crichton, David Koepp",
        "streaming": "Prime",
        "rating": 8.1,
        "userreviews": "7.8k",
        "metascore": 68,
        "popularity": 720,
        "description": "Dinosaurs are brought back to life in a theme park, but the experiment quickly becomes dangerous.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Jurassic+Park"
    },

    {
        "id": 19,
        "title": "Shrek",
        "duration": "1h 30m",
        "year": 2001,
        "agelimit": "PG",
        "genre": "Animation, Comedy, Adventure",
        "stars": "Mike Myers, Eddie Murphy, Cameron Diaz",
        "director": "Andrew Adamson, Vicky Jenson",
        "writers": "William Steig, Ted Elliott",
        "streaming": "Netflix",
        "rating": 7.9,
        "userreviews": "4.2k",
        "metascore": 84,
        "popularity": 650,
        "description": "An ogre embarks on a quest to rescue a princess and discovers an unexpected friendship.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Shrek"
    },

    {
        "id": 20,
        "title": "The Lion King",
        "duration": "1h 28m",
        "year": 1994,
        "agelimit": "G",
        "genre": "Animation, Adventure, Drama",
        "stars": "Matthew Broderick, Jeremy Irons, James Earl Jones",
        "director": "Roger Allers, Rob Minkoff",
        "writers": "Irene Mecchi, Jonathan Roberts",
        "streaming": "Disney+",
        "rating": 8.5,
        "userreviews": "5.9k",
        "metascore": 88,
        "popularity": 780,
        "description": "A lion cub must embrace his destiny as king after tragedy strikes his family.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=The+Lion+King"
    },

    {
        "id": 21,
        "title": "Finding Nemo",
        "duration": "1h 40m",
        "year": 2003,
        "agelimit": "G",
        "genre": "Animation, Adventure, Comedy",
        "stars": "Albert Brooks, Ellen DeGeneres, Alexander Gould",
        "director": "Andrew Stanton",
        "writers": "Andrew Stanton, Bob Peterson",
        "streaming": "Disney+",
        "rating": 8.1,
        "userreviews": "4.7k",
        "metascore": 90,
        "popularity": 710,
        "description": "A clownfish crosses the ocean to find his missing son.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Finding+Nemo"
    },

    {
        "id": 22,
        "title": "Coco",
        "duration": "1h 45m",
        "year": 2017,
        "agelimit": "PG",
        "genre": "Animation, Adventure, Fantasy",
        "stars": "Anthony Gonzalez, Gael García Bernal, Benjamin Bratt",
        "director": "Lee Unkrich, Adrian Molina",
        "writers": "Adrian Molina, Matthew Aldrich",
        "streaming": "Disney+",
        "rating": 8.4,
        "userreviews": "3.9k",
        "metascore": 81,
        "popularity": 690,
        "description": "A boy journeys to the Land of the Dead to uncover his family's history.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Coco"
    },

    {
        "id": 23,
        "title": "Black Panther",
        "duration": "2h 14m",
        "year": 2018,
        "agelimit": "PG-13",
        "genre": "Action, Superhero",
        "stars": "Chadwick Boseman, Michael B. Jordan, Lupita Nyong'o",
        "director": "Ryan Coogler",
        "writers": "Ryan Coogler, Joe Robert Cole",
        "streaming": "Disney+",
        "rating": 7.3,
        "userreviews": "6.5k",
        "metascore": 88,
        "popularity": 820,
        "description": "T'Challa returns to Wakanda to claim his throne and defend his nation.",
        "poster": "https://placehold.co/600x900/17182b/a78bfa?text=Black+Panther"
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
