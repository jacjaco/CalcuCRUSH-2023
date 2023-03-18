# """Script to seed database."""

# import os
# import json
# from random import choice, randint
# from datetime import datetime

# import crud
# import model
# import server

# os.system("dropdb ")
# # More code will go here
# os.system('dropdb ')
# os.system('createdb ')

# model.connect_to_db(server.app)
# model.db.create_all()

# with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
# movies_in_db = []
# for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime

    # TODO: create a movie here and append it to movies_in_db

    # title, overview, poster_path = (
    #     movie["title"],
    #     movie["overview"],
    #     movie["poster_path"],
    # )
    # release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    # db_movie = crud.create_movie(title, overview, release_date, poster_path)
    # movies_in_db.append(db_movie)

# model.db.session.add_all(movies_in_db)
# model.db.session.commit()