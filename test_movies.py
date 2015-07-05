#!/usr/bin/env python

import media
import unittest

# This test class verifies the Movie class initialization functionality

# Test values for Movie class member verification
title = 'Four Brothers'
imdb_id = 'tt0430105'
summary = 'Mark Wahlberg takes on a crime syndicate with his brothers.'
url1 = 'example.com/pic'
url2 = 'example.com/trailer'
rating = 5
lead_actors = ['Mark Wahlberg', 'Tyrese gibson']


class TestMovieClass(unittest.TestCase):
    def test_init_no_imdb_id(self):
        # Tests Movie init without OMDB lookup
        movie = media.Movie(title=title,
                            summary=summary,
                            trailer_youtube_url=url1,
                            poster_image_url=url2,
                            rating=rating,
                            lead_actors=lead_actors)
        self.assertEqual(movie.title, title)
        self.assertEqual(movie.summary, summary)
        self.assertEqual(movie.trailer_youtube_url, url1)
        self.assertEqual(movie.poster_image_url, url2)
        self.assertEqual(movie.rating, rating)
        self.assertEqual(movie.lead_actors, lead_actors)
        self.assertEqual(movie._webload_successful, False)

    def test_rating_limits(self):
        # Tests movie rating remains within 0 to 5 stars
        movie = media.Movie(rating=6)
        self.assertEqual(movie.rating, 5)
        movie = media.Movie(rating=-1)
        self.assertEqual(movie.rating, 0)
        movie = media.Movie(rating=None)
        self.assertEqual(movie.rating, 0)

    def test_init_with_imdb_id(self):
        # Verifies OMDB initialization
        movie = media.Movie(imdb_id=imdb_id)
        self.assertEqual(movie.title, title)
        self.assertEqual(movie._webload_successful, True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMovieClass)
unittest.TextTestRunner(verbosity=2).run(suite)
