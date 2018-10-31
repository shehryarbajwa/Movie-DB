import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story" , "A story of a boy and his toys that come to life" ,"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc") #These are instances in a class
avatar = media.Movie("42" , "A marine on an alien planet" , "http://religionnews.com/wp-content/uploads/2013/04/1600x1200_lookingback.jpg", "https://www.youtube.com/watch?v=I9RHqdZDCF0") #Instances in a class
batman = media.Movie("Dark Knight" , "A hero's journey to save his city" , "https://a.ltrbxd.com/resized/sm/upload/zu/51/m1/43/the-dark-knight-20-1200-1200-675-675-crop-000000.jpg?k=0a44472192" , "https://www.youtube.com/watch?v=GokKUqLcvD8")

group = [toy_story , avatar , batman]

fresh_tomatoes.open_movies_page(group)

print (toy_story.storyline)
batman.show_trailer
