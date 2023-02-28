#!/usr/bin/env python3
"""
File: 4-app.py
Desc: A simple flask application with babel extension
Author: Gizachew Bayness
Date Created: Feb 28, 2023
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config class for Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get the local language"""
    lcl = request.args.get('locale', None)
    if lcl and lcl in app.config['LANGUAGES']:
        return lcl
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """Home page"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
