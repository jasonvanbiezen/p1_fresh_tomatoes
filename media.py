import urllib2
import ast


class Movie:
    """
    Stores attributes of a movie including links to the poster art and a URL
    to the trailer on youtube.  If the imdb_id is provided, the rest of the
    attributes, except rating and trailer_youtube_url, will be obtained by
    querying the omdb api.  If imdb_id is not provided, or set to None, then
    the movie attributes must be provided in the contructor or set manually.

    Args:
        title: Movie Title
        summary: Short synopsis of the movie
        poster_image_url: URL to the movie's poster image
        trailer_youtube_url: URL to the movie's trailer on youtube
        rating: How you rate the movie (0-5)
        lead_actors: List of actor names
        genre: Genre of the movie
        released: date released (in date format: YYYY-MM-DD)
        imdb_id: If provided, all movie attributes except for rating and
trailer_youtube_url will be obtained from OMDB
     """
    VERSION = '1.0'
    OIMDB_URL = 'http://www.omdbapi.com'
    KEY_IMDB_ID = 'i'

    def __init__(self, title='Untitled', summary=None,
                 poster_image_url=None, trailer_youtube_url=None, rating=None,
                 lead_actors=[], genre=None, released=None, imdb_id=None):

        self.imdb_id = imdb_id
        self._webload_successful = False
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = rating or 0
        if self.rating > 5:
            self.rating = 5
        elif self.rating < 0:
            self.rating = 0

        # imdb_id provided, attempt to query omdb's API
        if self.imdb_id is not None:
            try:
                response = urllib2.urlopen(''.join([self.OIMDB_URL, '/?',
                                                    self.KEY_IMDB_ID, '=',
                                                    self.imdb_id]))
                info = ast.literal_eval(response.read())
                self.title = info['Title']
                self.summary = info['Plot']
                self.poster_image_url = info['Poster']
                self.lead_actors = info['Actors'].split(', ')
                self.genre = info['Genre']
                self.released = info['Released']
                # successfully retreived movie info
                self._webload_successful = True
            except urllib2.HTTPError, e:
                print(' '.join(["ERROR:", e.code,
                                ". Movie info could not be obtained from",
                                self.OIMDB_URL]))
            except urllib2.URLError, e:
                print(' '.join(["ERROR: Movie info could not be obtained from",
                      self.OIMDB_URL, ':']))
                for a in e.args:
                    print(a)

        # OMDB lookup failed or imdb_id not provided
        if not self._webload_successful:
            self.title = title
            self.summary = summary
            self.poster_image_url = poster_image_url
            self.lead_actors = lead_actors
            self.genre = genre
            self.released = released
