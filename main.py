movie_database = {
    "movie1": {
        "name": "Scream",
        "year": 1996,
        "director": "Wes Craven",
        "rating": 7.4,
},
    "movie2": {
        "name": "Funny Games",
        "year": 2007,
        "director": "Michael Haneke",
        "rating": 7.5,
    },
    "movie3": {
        "name": "Inception",
        "year": 2010,
        "director": "Christopher Nolan",
        "rating": 8.8,
    },
    "movie4": {
        "name": "Star Wars: Episode III - Revenge of the Sith",
        "year": 2005,
        "director": "George Lucas",
        "rating": 7.6,
    },
    "movie5": {
        "name": "Coraline",
        "year": 2009,
        "director": "Henry Selick",
        "rating": 7.8,

},
    "movie6": {
        "name": "The Fast and the Furious - Tokyo Drift",
        "year": 2006,
        "director": "Rob Cohen",
        "rating": 6.9,
    },
    "movie7": {
        "name": "Animal Farm",
        "year": 1954,
        "director": "Joy Batchelor, John Halas",
        "rating": 6.2,
    },
    "movie8": {
        "name": "American Psycho",
        "year": 2000,
        "director": "Mary Harron",
        "rating": 7.1,
    },
    "movie9": {
        "name": "Fractured",
        "year": 2019,
        "director": "Brad Anderson",
        "rating": 6.5,
    },
    "movie10": {
        "name": "The Truman Show",
        "year": 1998,
        "director": "Peter Weir",
        "rating": 8.2,
    }

}

#function to add a movie to the movie_database dictionary
def add_movie(database):
    movie_id = input("Enter the Movie ID: ")
    name = input("Enter the Movie Name: ")
    year = int(input("Enter the Year: "))
    director = input("Enter the Director: ")
    rating = float(input("Enter the Rating: "))

    database[movie_id] = {
        "name": name,
        "year": year,
        "director": director,
        "rating": rating
    }

#function to remove a movie from the movie_database dictionary
def remove_movie(database):
    movie_id = input("Enter the Movie ID: ")
    if movie_id in database:
        del database[movie_id]
    else:
        print("Movie ID not found")

#prompts the user to add or delete a movie
action = input("Do you want to add or delete a movie? (add/delete): ").strip().lower()

#calls to add or delete a movie
if action == "add":
    add_movie(movie_database)
elif action == "delete":
    remove_movie(movie_database)
else:
    pass

#formats the movie_database dictionary
for movie_id, movie_info in movie_database.items():
    print(f"{movie_id}:")
    for key, value in movie_info.items():
        print(f"{key}: {value}")
    print()

