#!/usr/bin/env python

import movies
import unittest

title='Four Brothers'
imdb_id='tt0430105'
summary='Mark Wahlberg takes on a crime syndicate with his brothers.'
url1='example.com/pic'
url2='example.com/trailer'
rating=10
lead_actors=['Mark Wahlberg','Tyrese gibson']

movie = movies.Movie(title,imdb_id,summary,url1,url2,rating,lead_actors)

class TestMovieClass(unittest.TestCase):
    def test_init(self):
        self.assertEqual(movie.title,title)
        self.assertEqual(movie.imdb_id,imdb_id)
        self.assertEqual(movie.summary,summary)
        self.assertEqual(movie.cover_url,url1)
        self.assertEqual(movie.trailer_url,url2)
        self.assertEqual(movie.rating,rating)
        self.assertEqual(movie.lead_actors,lead_actors)
        self.assertEqual(movie._webload_successful,False)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMovieClass)
unittest.TextTestRunner(verbosity=2).run(suite)

