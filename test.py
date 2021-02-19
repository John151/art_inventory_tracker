import unittest
from unittest import TestCase

import sqlite3
import config

test_db_path = 'test_art.sqlite'
config.db_path = test_db_path

import SQLDatabase as db
from model import Artist, Artwork

class TestDB(TestCase):

    def setUp(self):

        db.create_tables()
        # Deletes everything to start with empty database

        with sqlite3.connect(test_db_path) as conn:
            conn.execute('DELETE FROM artists')
        conn.close()

    def test_add_artist(self):
        example = Artist('Example', 'example@email.com')
        added = db.add_artist(example)

        self.assertTrue(added)

        expected_rows = [('Example', 'example@email.com')]
        actual_rows = self.get_all_data()

        self.assertEqual(expected_rows, actual_rows)



    def get_all_data(self):
        with sqlite3.connect(test_db_path) as conn:
            rows = conn.execute('SELECT * FROM artists').fetchall()
        conn.close()
        return rows

if __name__ == '__main__':
    unittest.main()