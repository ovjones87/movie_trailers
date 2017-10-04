import webbrowser

class Movie(object):
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	"""docstring for ClassName"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		#super(ClassName, self).__init__()
		#self.arg = arg
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)	