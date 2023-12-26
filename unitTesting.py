import unittest
import os
from app import app
from flask import Flask
from models.tables.users import User
import bcrypt
from configuration.seed import seed_db
from datetime import datetime
from configuration.config import db
from bs4 import BeautifulSoup

def get_csrf_token(page):
    soup = BeautifulSoup(page.data, 'html.parser')
    return soup.find('input', {'name': 'csrf_token'})['value']

class unitTest(unittest.TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        self.app = app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Voter Registration App', response.data)

    def test_login_get(self):
        response = self.app.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign in', response.data)

    def test_invalid_login(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'woah',
            'password': 'incorrect',
            'csrf_token': get_csrf_token(login_page)
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have entered an incorrect username or password, please try again.', response.data)

    def test_admin_login(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/user_panel/?user=1')
    
    def test_admin_homepage_get(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })

        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

    def test_admin_change_password(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })

        response = self.app.get('/admin_panel/?user=1')

        chg_psk_page = self.app.get('/user_panel/change_password/?username=admin')

        response = self.app.post('/user_panel/change_password/?username=admin', data={
            'current_password': 'admin',
            'new_password': 'admin1',
            'csrf_token': get_csrf_token(chg_psk_page)
        })

        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin1',
            'csrf_token': get_csrf_token(login_page)
        })
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

    def test_admin_navigate(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/admin_panel/voter_requests/?user=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Approval Page', response.data)

        response = self.app.get('/admin_panel/search_voters/?user=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Search', response.data)

        response = self.app.get('/admin_panel/manage_races/?user=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Races', response.data)

        response = self.app.get('/admin_panel/manage_candidates/?user=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Candidates', response.data)

        response = self.app.get('/admin_panel/manage_precincts/?user=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Precincts', response.data)

        response = self.app.get('/admin_panel/manage_poll_managers/?user=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Poll Managers', response.data)

        response = self.app.get('/admin_panel/manage_ballots/?user=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Ballots', response.data)

        response = self.app.get('/admin_panel/manage_zips/?user=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Zips', response.data)


    def test_manager_login(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'bigman',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/user_panel/?user=6')

    def test_manager_homepage(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'bigman',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })

        response = self.app.get('/manager_panel/?user=6')
        self.assertEqual(response.status_code, 200)
        
    def test_manager_navigate(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'bigman',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })
        response = self.app.get('/manager_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/admin_panel/voter_requests/?user=6')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Approval Page', response.data)

        response = self.app.get('/admin_panel/search_voters/?user=6')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Search', response.data)

    def test_admin_search(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })        
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        search_page = self.app.get('/admin_panel/search_voters/?user=1')
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/admin_panel/search_voters/?user=6', data={
            'first_name': 'jimmy',
            'csrf_token': get_csrf_token(search_page)
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jib', response.data)

    def test_admin_create_race(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })        
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        race_page = self.app.get('/admin_panel/manage_races/?user=1')
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/admin_panel/manage_races/?user=1', data={
            'name': 'oogabooga',
            'csrf_token': get_csrf_token(race_page)
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/admin_panel/manage_races/?user=1')

    def test_admin_add_candidate(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })        
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        candidate_page = self.app.get('/admin_panel/manage_candidates/?user=1')
        self.assertEqual(candidate_page.status_code, 200)

        response = self.app.post('/admin_panel/manage_candidates/?user=1', data={
            'first_name': 'Jerome',
            'last_name': 'Jeromeson',
            'party': 'dogs',
            'description': 'da dawgs',
            'csrf_token': get_csrf_token(candidate_page)
        })
        self.assertEqual(response.status_code, 302)

    def test_admin_add_precinct(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })        
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        precinct_page = self.app.get('/admin_panel/manage_precincts/?user=1')
        self.assertEqual(precinct_page.status_code, 200)

        response = self.app.post('/admin_panel/manage_precincts/?user=1', data={
            'voting_location': 'Bo James',
            'election_office': 'Joes Rooftop',
            'csrf_token': get_csrf_token(precinct_page)
        })
        self.assertEqual(response.status_code, 302)

    def test_admin_add_polling_manager(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })        
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        poll_page = self.app.get('/admin_panel/manage_poll_managers/?user=1')
        self.assertEqual(poll_page.status_code, 200)

        response = self.app.post('/admin_panel/manage_poll_managers/?user=1', data={
            'username': 'mojojojo',
            'email_address': 'mojojojo@mojojojo.mojo',
            'password': 'mojo',
            'csrf_token': get_csrf_token(poll_page)
        })
        self.assertEqual(response.status_code, 200)

    def test_admin_add_ballot(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })        
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        ballot_page = self.app.get('/admin_panel/manage_ballots/?user=1')
        self.assertEqual(ballot_page.status_code, 200)

        response = self.app.post('/admin_panel/manage_ballots/?user=1', data={
            'name': 'bbbbballot',
            'election': 'Example Election',
            'precinct': 'University Library',
            'csrf_token': get_csrf_token(ballot_page)
        })
        self.assertEqual(response.status_code, 200)

    def test_admin_add_zip(self):
        login_page = self.app.get('/login/')

        response = self.app.post("/login/", data={
            'username': 'admin',
            'password': 'admin',
            'csrf_token': get_csrf_token(login_page)
        })        
        response = self.app.get('/admin_panel/?user=1')
        self.assertEqual(response.status_code, 200)

        zips_page = self.app.get('/admin_panel/manage_zips/?user=1')
        self.assertEqual(zips_page.status_code, 200)

        response = self.app.post('/admin_panel/manage_zips/?user=1', data={
            'zip': '55555',
            'zip4start': '0000',
            'zip4end': '1337',
            'csrf_token': get_csrf_token(zips_page)
        })
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
