'''A collection of media types'''


class Movie(object):
    '''Movie Class contains movie elements used to generate a static webpage'''

    def __init__(
            self, movie_title, poster_image, trailer_youtube, movie_storyline):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.storyline = movie_storyline
