import os
from flask import request
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("BASE_URL")


class Links:
    def __init__(self, environment, route, name, args=None):
        self.environment = environment
        self.args = args
        if self.args is not None:
            self.routes = environment + route + "/?" + args
        else:
            self.routes = environment + route
        self.caption = name


def voter_routes(user):
    return [Links(base_url, "", "Home"), Links(base_url, "logout", "Logout", "user=" + user),
            Links(base_url, "user_panel", "My Account", "user=" + user)]

def voter_approved_routes(user):
    return [Links(base_url, "", "Home"), Links(base_url, "logout", "Logout", "user=" + user),
            Links(base_url, "user_panel", "My Account", "user=" + user),
            Links(base_url, "user_elections", "My Elections")]

def admin_routes(user):
    return [Links(base_url, "", "Home"),
            Links(base_url, "logout", "Logout", "user=" + user),
            Links(base_url, "admin_panel", "Admin Panel", "user=" + user),
            Links(base_url, "admin_panel/voter_requests", "Voter Requests", "user="+user),
            Links(base_url,"admin_panel/search_voters","Search Voters", "user="+user),
            Links(base_url,"admin_panel/manage_races","Manage Races","user="+user),
            Links(base_url,"admin_panel/manage_candidates","Manage Candidates","user="+user),
            Links(base_url,"admin_panel/manage_precincts","Manage Precincts","user="+user),
            Links(base_url,"admin_panel/manage_poll_managers","Manage Poll Managers","user="+user),
            Links(base_url,"admin_panel/manage_ballots","Manage Ballots","user="+user),
            Links(base_url,"admin_panel/manage_zips","Manage Zips","user="+user)]


def manager_routes(user):
    return [Links(base_url, "", "Home"),
            Links(base_url, "logout", "Logout", "user=" + user),
            Links(base_url, "manager_panel", "Manager Panel", "user=" + user),
            Links(base_url, "manager_panel/voter_requests", "Voter Requests", "user="+user),
            Links(base_url, "manager_panel/search_voters", "Search Voters", "user="+user),
            Links(base_url, "manager_panel/ballots","Ballots","user="+user)]

def guest_routes():
    return [Links(base_url, "", "Home"),
            Links(base_url, "login", "Login"),
            Links(base_url, "register", "Register")
            ]
