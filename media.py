import urllib2
import ast

class Movie:
    """ If the imdb_id argument is not None, the class will attempt to query the
    open imdb database and automatically assign the other variables.  The trailer_youtube_url
    and rating members will not be obtained from the open imdb"""
    VERSION='1.0'
    OIMDB_URL='http://www.omdbapi.com'
    KEY_IMDB_ID='i'

    def __init__(self,title='Untitled',summary=None,poster_image_url=None,trailer_youtube_url=None,rating=None,lead_actors=[],genre=None,released=None,imdb_id=None):
        self.imdb_id=imdb_id
        self._webload_successful=False
        self.trailer_youtube_url=trailer_youtube_url
        self.rating=rating

        if self.imdb_id!=None:
            try:
                response = urllib2.urlopen(''.join([self.OIMDB_URL,'/?',self.KEY_IMDB_ID,'=',self.imdb_id]))
                info = ast.literal_eval(response.read())
                self.title=info['Title']
                self.summary=info['Plot']
                self.poster_image_url=info['Poster']
                self.lead_actors=info['Actors'].split(', ')
                self.genre=info['Genre']
                self.released=info['Released']
                self._webload_successful=True
            except urllib2.HTTPError, e:
                print(' '.join(["ERROR:",e.code,". Movie info could not be obtained from",self.OIMDB_URL]))
            except urllib2.URLError, e:
                print(' '.join(["ERROR: Movie info could not be obtained from",self.OIMDB_URL,':']))
                for a in e.args:
                    print(a)

        if not self._webload_successful:        
            self.title=title
            self.summary=summary
            self.poster_image_url=poster_image_url
            self.rating=rating or 0
            self.lead_actors=lead_actors 
            self.genre=genre
            self.released=released

