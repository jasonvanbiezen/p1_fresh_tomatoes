import media


def get_movie_list():
    """
    Returns:
        A list of populated media.Movie objects
    """
    print("Generating movie list...")
    movie_list = []
    movie_list.append(media.Movie(
        title='Four Brothers',
        summary='Mark Wahlberg takes on a crime syndicate with his brothers.',
        trailer_youtube_url='https://www.youtube.com/watch?v=vZPi0K6UoP8',
        rating=5,
        imdb_id='tt0430105'))
    movie_list.append(media.Movie(
        'American Sniper',
        imdb_id='tt2179136',
        trailer_youtube_url='https://www.youtube.com/watch?v=5bP1f_1o-zo',
        rating=5))
    movie_list.append(media.Movie(
        imdb_id='tt0120657',
        trailer_youtube_url='https://www.youtube.com/watch?v=JYUBKcurY88',
        rating=4))
    movie_list.append(media.Movie(
        imdb_id='tt0416449',
        trailer_youtube_url='https://www.youtube.com/watch?v=UrIbxk7idYA',
        rating=5))
    movie_list.append(media.Movie(
        imdb_id='tt1790885',
        trailer_youtube_url='https://www.youtube.com/watch?v=k7R2uVZYebE',
        rating=5))
    movie_list.append(media.Movie(
        imdb_id='tt0119698',
        trailer_youtube_url='https://www.youtube.com/watch?v=4OiMOHRDs14',
        rating=5))
    print("Done!")
    return movie_list
