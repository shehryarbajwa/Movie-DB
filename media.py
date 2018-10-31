import webbrowser

class Movie(): #This is how to define a class
  def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube): #This is the constructor. It creates a new memory in the program for something new to be created
    self.title = movie_title #These are all instance variables
    self.storyline = movie_storyline #Unique to each object
    self.poster_image_url = poster_image #Made a universal declaration through self so we don't have to declare a new one each time we create an instance
    self.trailer_youtube_url = trailer_youtube

    def show_trailer(): #all methods associated with a class inside it are instance methods!
        webbrowser.open(self.trailer_youtube_url)
