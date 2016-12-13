import fresh_tomatoes
import media


Kung_Fu_Panda = media.Movie("Kung Fu Panda", "Prepare for Awesomeness", "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg","https://www.youtube.com/watch?v=PXi3Mv6KMzY", "5 Stars")

Kung_Fu_Panda_2 = media.Movie("Kung Fu Panda 2", "SKA2OOSH!", "https://upload.wikimedia.org/wikipedia/en/b/b1/Kung_Fu_Panda_2_Poster.jpg", "https://www.youtube.com/watch?v=oTtDn2W39Sg", "2 Thumbs Up")

Kung_Fu_Panda_3 = media.Movie("Kung Fu Panda 3", "The Weight is Over", "https://upload.wikimedia.org/wikipedia/en/e/e6/Kung_Fu_Panda_3_poster.jpg", "https://www.youtube.com/watch?v=10r9ozshGVE", "100% Certified Fresh")



movies = [Kung_Fu_Panda, Kung_Fu_Panda_2, Kung_Fu_Panda_3]

fresh_tomatoes.open_movies_page(movies)
