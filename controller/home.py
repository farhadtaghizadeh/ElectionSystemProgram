from flask import render_template
from controller.navigation import guest_routes
def home():
    return render_template('home.html', routes=guest_routes())