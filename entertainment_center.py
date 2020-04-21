import media
import fresh_tomatoes

We_Are_Champions = media.Movie("We Are Champions",
                               "https://www.i-media.tw/upload/news/welcome/16c6c12a2ff9a00673d185549ea992d6.jpg",
                               "https://www.youtube.com/watch?v=SKDUR7vV94U")
NINA_WU = media.Movie("NINA WU (ZHUO REN MI MI)","https://pic.pimg.tw/dreammaker790623/1563954273-3324877687_n.jpg","https://youtu.be/IRerp4-S9VI")

movies = [We_Are_Champions,NINA_WU]

fresh_tomatoes.open_movies_page(movies)