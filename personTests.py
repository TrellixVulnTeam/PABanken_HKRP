import unittest
from flask import Flask, render_template, request, url_for, redirect
from app import app
from models import db, Person

class PersonerTestCases(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        app.config["SERVER_NAME"] = "stefan.se"
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['WTF_CSRF_METHODS'] = []  # This is the magic
        app.config['TESTING'] = True

    def test_when_creating_new_should_validate_name_is_longer_than_three(self):
        test_client = app.test_client()
        url = '/personnew'
        with test_client:
            response = test_client.post(url, data={ "name":"12", "city":"Testar", "postalcode":"11122", "position":"g" })
            assert response.status_code != 302


    def test_when_creating_new_should_be_ok_when_name_is_longer_than_three(self):
        test_client = app.test_client()
        url = '/personnew'
        with test_client:
            response = test_client.post(url, data={ "name":"Stefan", "city":"Testar", "postalcode":"11122", "position":"g" })
            assert response.status_code == 302

    def test_when_creating_new_then_postalcode_should_be_larger_than_88888(self):
        test_client = app.test_client()
        url = '/personnew'
        with test_client:
            response = test_client.post(url, data={ "name":"Stefan", "city":"Testar", "postalcode":"88899", "position":"g" })
            assert response.status_code != 302

    def test_when_creating_new_then_postalcode_should_be_less_than_88888(self):
        test_client = app.test_client()
        url = '/personnew'
        with test_client:
            response = test_client.post(url, data={ "name":"Stefan", "city":"Testar", "postalcode":"11188", "position":"g" })
            assert response.status_code == 302


if __name__ == "__main__":
    unittest.main()