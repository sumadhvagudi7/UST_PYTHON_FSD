"""
--------------------------------------------------------
StreamFlix: Video Streaming Optimization System
--------------------------------------------------------
Objective:
- Use Flyweight Pattern to share movie metadata among users
- Use Proxy Pattern to cache remote video content
--------------------------------------------------------
"""

import time
import random

# ----------------------------
# Flyweight Pattern
# ----------------------------
class MovieFlyweight:
    """Shared movie metadata (intrinsic data)"""
    def __init__(self, title, genre, director, duration):
        self.title = title
        self.genre = genre
        self.director = director
        self.duration = duration

    def display_info(self):
        """Display movie details"""
        print(f"\nMovie: {self.title}")
        print(f"   Genre: {self.genre}")
        print(f"   Director: {self.director}")
        print(f"   Duration: {self.duration}")


class MovieFactory:
    """Creates or reuses shared MovieFlyweight objects"""
    _movies = {}

    @staticmethod
    def get_movie(title, genre, director, duration):
        key = (title, genre, director, duration)
        if key not in MovieFactory._movies:
            print(f"Creating new flyweight for '{title}'")
            MovieFactory._movies[key] = MovieFlyweight(title, genre, director, duration)
        else:
            print(f"Reusing existing flyweight for '{title}'")
        return MovieFactory._movies[key]


# ----------------------------
# Proxy Pattern
# ----------------------------
class VideoService:
    """Simulates slow, costly video fetching"""
    def fetch_video(self, movie_title):
        print(f"\nFetching video stream for '{movie_title}' from remote server...")
        time.sleep(random.uniform(1, 2))  # Simulate delay since no apis are available
        return f"{movie_title} - [Video Stream Data]"


class VideoProxy:
    """Proxy adds caching to reduce redundant fetches"""
    def __init__(self):
        self._cache = {}
        self._video_service = VideoService()

    def get_video(self, movie_title):
        if movie_title in self._cache:
            print(f"Retrieved '{movie_title}' from cache.")
        else:
            print(f"'{movie_title}' not in cache, fetching from video service...")
            self._cache[movie_title] = self._video_service.fetch_video(movie_title)
            print(f"Cached '{movie_title}' for future use.")
        return self._cache[movie_title]


# ----------------------------
# User Session
# ----------------------------
class UserSession:
    """Represents a user watching a movie"""
    def __init__(self, user_name, movie_flyweight, video_proxy):
        self.user_name = user_name
        self.movie_flyweight = movie_flyweight
        self.video_proxy = video_proxy

    def watch_movie(self):
        print(f"\n {self.user_name} is now watching '{self.movie_flyweight.title}'")
        self.movie_flyweight.display_info()
        video_data = self.video_proxy.get_video(self.movie_flyweight.title)
        print(f"{self.user_name} started streaming: {video_data}")


# ----------------------------
# Main Execution (Testing)
# ----------------------------
if __name__ == "__main__":
    # Step 1: Create Proxy
    video_proxy = VideoProxy()

    # Step 2: Create or reuse movie flyweights
    movie1 = MovieFactory.get_movie("Inception", "Sci-Fi", "Christopher Nolan", "2h 28m")
    movie2 = MovieFactory.get_movie("Inception", "Sci-Fi", "Christopher Nolan", "2h 28m")

    print(f"\n Flyweight objects created: {len(MovieFactory._movies)}")

    # Step 3: Create User Sessions
    user1 = UserSession("Alice", movie1, video_proxy)
    user2 = UserSession("Bob", movie2, video_proxy)

    # Step 4: Simulate watching
    user1.watch_movie()
    user2.watch_movie()
