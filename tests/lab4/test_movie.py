import unittest
import sys
sys.path.append(r'C:\Users\Даниил\Desktop\cs-102')

from src.lab4.movie import Cinema


cinema = Cinema(r"tests\lab4\films.txt", r"tests\lab4\history.txt", "1,2,3")

class TestCinema(unittest.TestCase):
    def test_load_films(self):
        expected_films = {1: 'Мстители: Финал', 2: 'Хатико',
                          3: 'Дюна', 4: 'Унесенные призраками'}
        self.assertEqual(cinema.load_films(), expected_films)

    def test_load_history(self):
        expected_history = [[2, 1, 3], [1, 4, 3], [2, 2, 2, 2, 2, 3]]
        self.assertEqual(cinema.load_history(), expected_history)

    def test_filter_users(self):
        expected_filtered_users = [[2, 1, 3]]
        self.assertEqual(cinema.filter_users(), expected_filtered_users)

    def test_exclude_watched_films(self):
        filtered_users = cinema.filter_users()
        expected_unwatched_films = []
        self.assertEqual(cinema.exclude_watched_films(
            filtered_users), expected_unwatched_films)


if __name__ == 'main':
    unittest.main()