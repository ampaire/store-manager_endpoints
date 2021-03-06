import json
import unittest

from app.get_an_entry import app
from flask import Flask, request


class TestGetOne(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True

    def test_can_get_an_entry(self):
        response = self.client.get("/api/v1/entries/1")
        self.assertEqual(response.status_code, 200)

    def test_JSON_format(self):
        response = self.client.get('/api/v1/entries',
                                   data="This isn't a json but it's a string!")
        self.assertEqual(response.status_code, 404)

    def test_cannot_get_nonexisting(self):
        response = self.client.get('/api/v1/entries/6')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
