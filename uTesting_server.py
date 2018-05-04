import os
import unittest

from setup import create_app, setup_database
from models import User
# Parts tested
from Database import db
import helpers


# Test Class
class FlaskTestCase(unittest.TestCase):
    """ Setup and login/out. """

    def setUp(self):
        self.client_auth = {"name": "test", "password": "password123"}

        self.client = create_app()
        self.client.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.client.config['WTF_CSRF_ENABLED'] = False
        self.client.testing = True

        if not os.path.isfile('test.db'):
            setup_database(self.client)
        self.app = self.client.test_client()
        # Always start with 1 valid user.
        with self.client.app_context():
            u = User(self.client_auth['name'], self.client_auth['password'])
            u.commit_self()

    def login(self, name=None, password=None):
        if name is None:
            name = self.client_auth['name']
        if password is None:
            password = self.client_auth['password']
        return self.app.post('/login', content_type='multipart/form-data', data=dict(name=name, password=password),
                             follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def tearDown(self):
        # User must be removed after each test, otherwise it fails.
        os.remove("test.db")
        pass

    # ==============================================================================

    """ Flask run & logging in/out. """

    def test_basic(self):
        """ >> Check the app starts and can be called upon. """
        p = self.app.get("/")
        assert b'<title>Home</title>' in p.data
        self.assertEqual(200, p.status_code)

    def test_login_and_logout(self):
        """ >> Login and logout again, including bad auth response. """
        lg = self.login()
        assert b'You have been logged in.' in lg.data
        self.assertEqual(200, lg.status_code)

        lg = self.logout()
        assert b'You have been logged out.' in lg.data
        self.assertEqual(200, lg.status_code)

        lg = self.login(password="hErTzIaN321")
        assert b'Incorrect name/password combination given.' in lg.data
        self.assertEqual(200, lg.status_code)


################################################################################
# Execute tests
if __name__ == '__main__':
    unittest.main(verbosity=2)