import fresh_tomatoes
import media

# Declaration of the movs Dictionary, containing the variety of movies from our library.
movs = {
    # For further information of the declaration of a Movie, please see the Movie Class in media.py
    media.Movie("Toy Story", "Bla bla bla the storyline", "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc"),
    media.Movie("Avatar", "Bla bla bla the storyline", "http://www.impawards.com/2009/posters/avatar_xlg.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY"),
    media.Movie("Jason Bourne", "Bla bla bla the storyline", "http://www.joblo.com/timthumb.php?src=/posters/images/full/jason-bourne-poster-A.jpg&h=600&q=100", "https://www.youtube.com/watch?v=F4gJsKZvqE4"),
    media.Movie("Scarface", "Bla bla bla the storyline", "https://ciereszko.files.wordpress.com/2013/09/scarface-poster-al-pacino-movie-poster.jpg", "https://www.youtube.com/watch?v=7pQQHnqBa2E")
}

# Using the fresh_tomatoes module to have the HTML template set up.
fresh_tomatoes.open_movies_page(movs)
