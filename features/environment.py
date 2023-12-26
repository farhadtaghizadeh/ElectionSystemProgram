import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler

import flask
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

FIREFOX_DRIVER=("/usr/bin/firefox")



firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument('--no-proxy-server')
firefox_options.add_argument("--proxy-server='direct://'")
firefox_options.add_argument("--proxy-bypass-list=*")


def before_all(context):
    context.server = simple_server.WSGIServer(("", 5001), WSGIRequestHandler)
    context.server.set_app(flask.current_app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()
    context.browser = webdriver.Firefox(options=firefox_options)
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_all(context):
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()
