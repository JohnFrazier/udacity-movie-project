#!/usr/bin/python2
# coding=UTF-8

import media
import fresh_tomatoes

"""entertainment_center.py:
This is the entry point for this application. It supplies
movie data and launches fresh_tomatoes.open_movies_page()"""


""" MOVIE_LIST is a "Database" of Movie instances from media.py
 (self, movie_title, poster_image, trailer_youtube, movie_storyline)"""

MOVIE_LIST = [
    media.Movie(
        "Wolf Children",
        "https://upload.wikimedia.org/wikipedia/en/9/9c/%C5%8Ckami_Kodomo_no"
        "_Ame_to_Yuki_poster.jpg",
        "https://www.youtube.com/watch?v=8SlB-SpDMKI",
        "The story follows a young mother who is left to raise two werewolf "
        "children after their werewolf father dies."),


    media.Movie(
        "Get Low",
        "https://upload.wikimedia.org/wikipedia/en/2/2c/Get_Low_Poster.jpg",
        "https://www.youtube.com/watch?v=C25TG5kLJGw",
        "Get Low is a 2010 drama film about a Tennessee hermit in the 1930s "
        "who throws his own funeral party while still alive."),

    media.Movie(
        "Garden State",
        "https://upload.wikimedia.org/wikipedia/en/3/3c/Garden_State_Poster"
        ".jpg",
        "https://www.youtube.com/watch?v=u82n0e1mgmQ",
        "Garden State is a 2004 comedy-drama film written and directed by "
        "Zach Braff and starring Natalie Portman, Peter Sarsgaard, Ian Holm "
        "and Braff himself. The film centers on Andrew Largeman (Braff), a "
        "26-year-old actor/waiter who returns to his hometown in New Jersey "
        "after his mother dies. Braff based the film on his real life "
        "experieces."),

    media.Movie(
        "Princess Mononoke",
        "https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_J"
        "apanese_Poster_%28Movie%29.jpg",
        "https://www.youtube.com/watch?v=4OiMOHRDs14",
        "Princess Mononoke is set in the late Muromachi period (approximately "
        "1336 to 1573) of Japan with fantasy elements. The story follows the "
        "young Emishi warrior Ashitaka's involvement in a struggle between "
        "forest gods and the humans who consume its resources. The term "
        "\"Mononoke\" (物の怪 or もののけ?) is not a name, but a Japanese "
        "word for a spirit or monster.")]


def run():
    """run the page generator and open it in a browser"""
    fresh_tomatoes.open_movies_page(MOVIE_LIST)

if __name__ == '__main__':
    # only start if executed directly not when loaded as a module.
    print MOVIE_LIST[3].storyline
    run()

