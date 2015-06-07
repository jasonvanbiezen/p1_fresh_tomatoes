#!/usr/bin/env python

import movies
import fresh_tomatoes

if __name__=='__main__':
    my_movies = movies.get_movie_list()
    fresh_tomatoes.open_movies_page(my_movies)

