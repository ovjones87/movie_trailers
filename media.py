import webbrowser
# defines a class for each instance of a Movie object"""


class Movie(object):

    # VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    """ this docstring is the constructor for each instance of the following objects"""  # NOQA
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    """This docstring opens the webbroswer and runs the trailers"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)