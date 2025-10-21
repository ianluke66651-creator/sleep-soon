import unittest
from src.app.services.spotify_client import SpotifyClient
from src.app.services.youtube_client import YouTubeClient

class TestServices(unittest.TestCase):

    def setUp(self):
        self.spotify_client = SpotifyClient()
        self.youtube_client = YouTubeClient()

    def test_spotify_client_initialization(self):
        self.assertIsNotNone(self.spotify_client)

    def test_youtube_client_initialization(self):
        self.assertIsNotNone(self.youtube_client)

    def test_spotify_data_retrieval(self):
        data = self.spotify_client.get_listening_data()
        self.assertIsInstance(data, dict)
        self.assertIn('listening_time', data)

    def test_youtube_data_retrieval(self):
        data = self.youtube_client.get_watch_hours()
        self.assertIsInstance(data, dict)
        self.assertIn('watch_hours', data)

if __name__ == '__main__':
    unittest.main()