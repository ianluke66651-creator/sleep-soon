import unittest
from src.app.analytics.sleep_analysis import analyze_sleep_data

class TestSleepAnalysis(unittest.TestCase):

    def test_good_sleep_cycle(self):
        sleep_data = {
            'sleep_start': '22:30',
            'sleep_end': '06:30',
            'spotify_usage': 1.5,  # hours
            'youtube_usage': 0.5    # hours
        }
        result = analyze_sleep_data(sleep_data)
        self.assertEqual(result['sleep_quality'], 'Good')
        self.assertIn('Consider maintaining this routine', result['suggestions'])

    def test_bad_sleep_cycle(self):
        sleep_data = {
            'sleep_start': '01:00',
            'sleep_end': '07:00',
            'spotify_usage': 3.0,  # hours
            'youtube_usage': 2.0     # hours
        }
        result = analyze_sleep_data(sleep_data)
        self.assertEqual(result['sleep_quality'], 'Poor')
        self.assertIn('Try to sleep earlier', result['suggestions'])

    def test_no_sleep_data(self):
        sleep_data = {
            'sleep_start': None,
            'sleep_end': None,
            'spotify_usage': 0.0,
            'youtube_usage': 0.0
        }
        result = analyze_sleep_data(sleep_data)
        self.assertEqual(result['sleep_quality'], 'No Data')
        self.assertIn('Please track your sleep', result['suggestions'])

if __name__ == '__main__':
    unittest.main()