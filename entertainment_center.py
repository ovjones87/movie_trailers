import fresh_tomatoes
import media

# Captain Underpants: movie title, storyline, poster image and movie trailer
Captain_Underpants = media.Movie(
    "Captain Underpants",
    "George Beard and Harold Hutchins are two overly imaginative"
    "pranksters who spend hours in a treehouse creating comic books.",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcSe2w-CmmAEZb_hRRq2EGrl5G1PC0tn2snNDO-S9c__Jz66uRjC",  # NOQA
    "https://www.youtube.com/watch?v=NP8TA3d_zvQ")

# Jumanji: movie title, storyline, poster image and movie trailer
Jumanji_Welcome_to_the_Jungle = media.Movie(
    "Jumanji: Welcome to the Jungle",
    "Four high school kids discover an old video"
    "game console and are drawn into the game",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcSJir3ifd1WldB6AfldmvA08D8jsv6t7ScNBeM5keJoE3CQsJa1",  # NOQA
    "https://www.youtube.com/watch?v=sNGbd-i8wR0"
    )

# The Lego Batman Movie: movie title, storyline, poster image and movie trailer
The_Lego_Batman_Movie = media.Movie(
    "The Lego Batman Movie",
    "There are big changes brewing in Gotham, but if Batman (Will Arnett)wants"
    "to save the city from the Joker's (Zach Galifianakis) hostile takeover",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcS-ysr5T3p--mS7aTE5KvaSnmM6CosK9_D-znWs_fbTNVgizHhv",  # NOQA
    "https://www.youtube.com/watch?v=ZQlfyj5bH-M"
    )

# The Lego Ninjago: movie title, storyline, poster image and movie trailer
The_LEGO_Ninjago_Movie = media.Movie(
    "The LEGO Ninjago Movie",
    "The battle for NINJAGO City calls to action young Master Builder Lloyd,"
    "aka the Green Ninja, along with his friends, also secret ninja warriors.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcRIesCVWOiAc5bBYwhQuBzARQeuDxTQuBTeHHM442L61X_F78wl",  # NOQA
    "https://www.youtube.com/watch?v=sZSYYiATFTI"
    )

# The Emoji Movie: movie title, storyline, poster image and movie trailer
The_Emoji_Movie = media.Movie(
    "The Emoji Movie",
    "Hidden inside a smartphone, the bustling city of Textopolis is home to"
    "all emojis.Each emoji has only one facial expression, except for Gene,"
    "an exuberant emoji with multiple expressions. ",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcRQc0pj8eAuiJa5K_DX1MeTSWwQCX5mDaBWz8auP38FeUX7NX5V",  # NOQA
    "https://www.youtube.com/watch?v=o_nfdzMhmrA"
    )

# Despicable Me 3: movie title, storyline, poster image and movie trailer
Despicable_Me_3 = media.Movie(
    "Despicable Me 3",
    "The mischievous Minions hope that Gru will return to a life of"
    "crime after the new boss of the Anti-Villain League fires him.",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcTg3JQThacqbSPauObMc700jNW_GTAd-e9DAV_QIWvMYq8v3mVx",  # NOQA
    "https://www.youtube.com/watch?v=UReNQAdei4Y"
    )

# Set the movies that will be passed to the media file
movies = [
    Captain_Underpants, The_LEGO_Ninjago_Movie, The_Emoji_Movie,
    Jumanji_Welcome_to_the_Jungle, The_Lego_Batman_Movie, Despicable_Me_3
    ]

fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)