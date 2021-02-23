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

    # tests for artist table---------------------------------
    # tests for adding new artist
    def test_add_new_artist(self):
        # example 1 valid data
        example = Artist('Example', 'example@email.com')

        added = db.add_artist(example)
        self.assertTrue(added)

        expected_rows = [('Example', 'example@email.com')]
        actual_rows = self.get_all_data_artists()
        self.assertEqual(expected_rows, actual_rows)

        # example 2 valid data
        example2 = Artist('Example2', 'example@email.com')

        added = db.add_artist(example2)
        self.assertTrue(added)

        expected_rows = [('Example', 'example@email.com'), ('Example2', 'example@email.com')]
        actual_rows = self.get_all_data_artists()
        self.assertEqual(expected_rows, actual_rows)

    # test for adding duplicate artist
    def test_add_duplicate_artist(self):
        example = Artist('Example', 'example@email.com')
        added = db.add_artist(example)
        self.assertTrue(added)

        example2 = Artist('Example', 'different_example@email.com')
        added2 = db.add_artist(example2)
        self.assertFalse(added2)

        expected_rows = [('Example', 'example@email.com')]
        actual_rows = self.get_all_data_artists()
        self.assertCountEqual(expected_rows, actual_rows)

    # test for getting latest artist ID
    def test_get_latest_artist_id(self):
        example = Artist('Example', 'example@email.com')
        db.add_artist(example)
        example2 = Artist('Example2', 'example2@email.com')
        db.add_artist(example2)

        expected_max_id = 2
        actual_max_id = db.get_max_rowID()
        self.assertEqual(expected_max_id, actual_max_id)

    # tests for artwork table--------------------------------


    # utility functions---------------------------------------

    def get_all_data_artists(self):
        with sqlite3.connect(test_db_path) as conn:
            rows = conn.execute('SELECT * FROM artists').fetchall()
        conn.close()
        return rows

    def get_all_data_artwork(self):
        with sqlite3.connect(test_db_path) as conn:
            rows = conn.execute('SELECT * FROM artwork').fetchall()
        conn.close()
        return rows

if __name__ == '__main__':
    unittest.main()