
class Movie:
    """ If the imdb_id argument is not None, the class will attempt to query the
    omdb database and automatically assign the other variables."""
    VERSION='1.0'
    def __init__(self,title='Untitled',summary=None,cover_url=None,trailer_url=None,rating=None,lead_actors=[],imdb_id=None):
        self.title=title
        self.imdb_id=imdb_id
        self.summary=summary
        self.cover_url=cover_url
        self.trailer_url=trailer_url
        self.rating=rating
        self.lead_actors=lead_actors 
        self._webload_successful=False


def get_movie_list():
    ret = []
    ret.append(Movie('Four Brothers','Mark Wahlberg takes on a crime syndicate with his brothers.','http://ia.media-imdb.com/images/M/MV5BMTU4NzM3Njg2NV5BMl5BanBnXkFtZTcwNjU4NDczMw@@._V1_SY317_CR0,0,214,317_AL_.jpg','https://www.youtube.com/watch?v=vZPi0K6UoP8',5,'tt0430105'))
    ret.append(Movie('American Sniper',imdb_id='tt2179136'))

