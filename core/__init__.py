import os
from flask import Flask, render_template, flash, request, session, g, redirect, url_for, abort, jsonify, make_response
from flask_bootstrap import Bootstrap
from core.plot.views import plotter

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(__name__)

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'graphing.db'),
        DEBUG=True,
        SECRET_KEY='_\xcb\xa0\x04\xd9?\x81G\xc9\xb8+\xc7C\xb9,\xed\x8f\xe8\x14\xaf8\xab\x10\x4a',
        USERNAME='admin',
        PASSWORD='abc123'
    ))
    app.config.from_envvar('FLASK_GRAPHING_SETTINGS', silent=True)
    app.register_blueprint(plotter, url_prefix='/plotter')
    return app

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')