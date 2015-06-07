#!/usr/bin/env python

import entertainment_center
import fresh_tomatoes

if __name__=='__main__':
    my_movies = entertainment_center.get_movie_list()
    fresh_tomatoes.open_movies_page(my_movies)

