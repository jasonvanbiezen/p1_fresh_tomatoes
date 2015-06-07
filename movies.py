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


def get_movie_list():
    print("Generating movie list...")
    ret = []
    ret.append(Movie(title='Four Brothers',summary='Mark Wahlberg takes on a crime syndicate with his brothers.',poster_image_url='http://ia.media-imdb.com/images/M/MV5BMTU4NzM3Njg2NV5BMl5BanBnXkFtZTcwNjU4NDczMw@@._V1_SY317_CR0,0,214,317_AL_.jpg',trailer_youtube_url='https://www.youtube.com/watch?v=vZPi0K6UoP8',rating=5,imdb_id='tt0430105'))
    ret.append(Movie('American Sniper',imdb_id='tt2179136',trailer_youtube_url='https://www.youtube.com/watch?v=5bP1f_1o-zo',rating=5)),
    ret.append(Movie(imdb_id='tt0120657',trailer_youtube_url='https://www.youtube.com/watch?v=JYUBKcurY88',rating=4))
    ret.append(Movie(imdb_id='tt0416449',trailer_youtube_url='https://www.youtube.com/watch?v=UrIbxk7idYA',rating=5))
    ret.append(Movie(imdb_id='tt1790885',trailer_youtube_url='https://www.youtube.com/watch?v=k7R2uVZYebE',rating=5))
    ret.append(Movie(imdb_id='tt0119698',trailer_youtube_url='https://www.youtube.com/watch?v=4OiMOHRDs14',rating=5))
    print("Done!")
    return ret

