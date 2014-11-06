#!/usr/bin/env python

import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        rv = self.app.get('/')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)

    def test_hello_page(self):
        rv = self.app.get('/hello/')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)

    def test_default_redirecting(self):
        rv = self.app.get('hello')
        self.assertEqual(rv.status_code, 301)

    def test_static_text_file_request(self):
        rv = self.app.get('/robots.txt')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)
        rv.close()

if __name__ == '__main__':
    unittest.main()
