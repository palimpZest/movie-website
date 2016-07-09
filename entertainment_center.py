import fresh_tomatoes
import media

# media.Movie calls the __init__ function defined inside the class Movie()
true_romance = media.Movie("True Romance",
                           "Clarence and Alabama try to flee a mafia gang.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d6/True_romance.jpg",  # noqa
                           "https://www.youtube.com/watch?v=_wNYNDzKpuQ")

the_thin_red_line = media.Movie("The Thin Red Line",
                                "Soldiers fighting at Guadalcanal during WW2.",
                                "https://upload.wikimedia.org/wikipedia/en/a/ae/The_Thin_Red_Line_Poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=ejm0XvT3rB8")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns about the true nature of "
                         "reality and those who control it.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=tGgCqGm_6Hs")

serpico = media.Movie("Serpico",
                      "The true story of a honest cop in a corrupt "
                      "police department.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Serpico_imp.jpg",  # noqa
                      "https://www.youtube.com/watch?v=nBJQ1pK372Q")

wings_of_desire = media.Movie("Wings of Desire",
                              "An angel tries to become a human being when "
                              "he falls in love.",
                              "https://upload.wikimedia.org/wikipedia/en/7/74/Wingsofdesireposter.jpg",  # noqa
                              "https://www.youtube.com/watch?v=dwo122meoAA")

the_big_lebowski = media.Movie("The Big Lebowski",
                               "The Dude seeks restitution for his ruined rug "
                               "and enlists his bowling buddies to help "
                               "get it.",
                               "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",  # noqa
                               "https://www.youtube.com/watch?v=cd-go0oBF4Y")

breathless = media.Movie("Breathless",
                         "A thief wanted by authorities attempts to persuade "
                         "a hip american journalist student to go to Italy.",
                         "https://upload.wikimedia.org/wikipedia/en/3/3f/%C3%80_bout_de_souffle_%28movie_poster%29.jpg",  # noqa
                         "https://www.youtube.com/watch?v=WCDEAu4R8hA")

millers_crossing = media.Movie("Miller's Crossing",
                               "Tom Regan tries to keep peace between warring "
                               "mobs during the Prohibition.",
                               "https://upload.wikimedia.org/wikipedia/en/2/2b/Millerscrossingposter.jpg",  # noqa
                               "https://www.youtube.com/watch?v=qYQNlJ5zrWA")

scott_pilgrim_vs_the_world = media.Movie("Scott Pilgrim vs. the World",
                                         "Scott Pilgrim must defeat his new "
                                         "girlfriend's seven evil exes in "
                                         "order to win her heart.",
                                         "https://upload.wikimedia.org/wikipedia/en/1/14/Scott_Pilgrim_vs._the_World_teaser.jpg",  # noqa
                                         "https://www.youtube.com/watch?v=7wd5KEaOtm4")  # noqa

fight_club = media.Movie("Fight Club",
                         "Don't Ever Talk About It.",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=BdJKm16Co6M")

shaun_of_the_dead = media.Movie("Shaun of the Dead",
                                "A man decides to turn his moribund life "
                                "around as the dead return to eat the living.",
                                "https://upload.wikimedia.org/wikipedia/en/e/ec/Shaun-of-the-dead.jpg",  # noqa
                                "https://www.youtube.com/watch?v=OMitSKT-u_k")

drive = media.Movie("Drive",
                    "A mysterious Hollywood stuntman finds himself trouble "
                    "when he helps out his neighbor.",
                    "https://upload.wikimedia.org/wikipedia/en/1/13/Drive2011Poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=KBiOF3y1W0Y")

batman_begins = media.Movie("Batman Begins",
                            "After training with his mentor, Batman begins "
                            "his war on crime in Gotham City.",
                            "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=QhPqez3CwiM")

big_hero_6 = media.Movie("Big Hero 6",
                         "Inflatable robot Baymax, and prodigy Hiro Hamada "
                         "team up with a group of friends to form a band of "
                         "high-tech heroes.",
                         "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",   # noqa
                         "https://www.youtube.com/watch?v=z3biFxZIJOQ")

the_royal_tenembaums = media.Movie("The Royal Tenembaums",
                                   "An estranged family of former child "
                                   "prodigies reunites when their father "
                                   "announces he is terminally ill.",
                                   "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Tenenbaums.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=8Eg6yIwP2vs")  # noqa

taxi_driver = media.Movie("Taxi Driver",
                          "A mentally unstable Vietnam War veteran works as a "
                          "night-time taxi driver in New York City.",
                          "https://upload.wikimedia.org/wikipedia/en/c/c9/Taxi_Driver_poster.JPG",  # noqa
                          "https://www.youtube.com/watch?v=UUxD4-dEzn0")

birdman = media.Movie("Birdman",
                      "A former popular actor's struggle to cope with his "
                      "current life as a wasted actor.",
                      "https://upload.wikimedia.org/wikipedia/en/a/a3/Birdman_poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=uJfLoE6hanc")

whiplash = media.Movie("Whiplash",
                       "A promising young drummer enrolls at a music "
                       "conservatory where his instructor will stop at "
                       "nothing to realize his potential.",
                       "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=aHDEZXoh4-c")

movies = [true_romance, the_thin_red_line, the_matrix, serpico,
          wings_of_desire, the_big_lebowski, breathless, millers_crossing,
          scott_pilgrim_vs_the_world, fight_club, shaun_of_the_dead, drive,
          batman_begins, big_hero_6, the_royal_tenembaums, taxi_driver,
          birdman, whiplash]
# opens fresh tomatoes file with the movies list.
fresh_tomatoes.open_movies_page(movies)
