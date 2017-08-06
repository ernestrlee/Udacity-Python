import media
import fresh_tomatoes

# create each instance of a movie with the movie title, storyline,
# poster URL, and trailer URL
braveheart = media.Movie("Braveheart",
                         "A story of a Scottish hero leading his men to "
                         "freedom.",
                         "https://upload.wikimedia.org/wikipedia/en/5/55/"
                         "Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=1cnoM8EiGGU")

gladiator = media.Movie("Gladiator",
                        "A story of how a general became a Gladiator.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/"
                        "Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")

zorro = media.Movie("The Mask of Zorro",
                    "The story of a man becoming the legend of Zorro.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/5/52/"
                    "Mask_of_zorro.jpg/220px-Mask_of_zorro.jpg",
                    "https://www.youtube.com/watch?v=uczLtpWF_cY")

shawshank = media.Movie("The Shawshank Redemption",
                        "The story of an innocent man and his escape from "
                        "prison.",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/"
                        "ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

passengers = media.Movie("Passengers",
                         "The story of a man and woman finding themselves "
                         "prematurely awoken on a spaceship.",
                         "https://upload.wikimedia.org/wikipedia/en/8/8e/"
                         "Passengers_2016_film_poster.jpg",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")

the_rock = media.Movie("The Rock",
                       "The story of man trying to stop attackers on Alcatraz "
                       "with the help of a known criminal.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/8/82/"
                       "The_Rock_%28movie%29.jpg/"
                       "220px-The_Rock_%28movie%29.jpg",
                       "https://www.youtube.com/watch?v=313n0wga2xo")

# create a list of movie objects from the movies created above that will be
# sent to fresh_tomatoes
movies = [braveheart, gladiator, zorro, shawshank, passengers, the_rock]

# use the open movies page method, passing in the list of movie objects
fresh_tomatoes.open_movies_page(movies)
