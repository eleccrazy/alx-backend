#!/usr/bin/env python3
"""
File: 1-app.py
Desc: A simple flask application with babel extension
Author: Gizachew Bayness
Date Created: Feb 28, 2023
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """Config class for configuring languages and timezons"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def home():
    """Handles the home route of the flask application"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
