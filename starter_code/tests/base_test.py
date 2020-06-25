""""
This class should be the parent class non-unit test.

It allows for instantiation of the database dynamically

and makes sure that it is a new, blank database each time.


"""
from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()

        self.app_context = app.test_client()
        self.app_context = app.app_context()

        pass

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
        pass
