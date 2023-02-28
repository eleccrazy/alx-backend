#!/usr/bin/env python3
"""
File: 4-app.py
Desc: A simple flask application with babel extension
Author: Gizachew Bayness
Date Created: Feb 28, 2023
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """Config class for configuring languages and timezons"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


# @babel.localeselector
def get_locale():
    """Determines the best match with our supported languages."""
    lcl = request.args.get('locale', None)
    if lcl and lcl in app.config['LANGUAGES']:
        return lcl
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home():
    """Handles the home route of the flask application"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
