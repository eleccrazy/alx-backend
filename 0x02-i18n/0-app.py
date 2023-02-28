#!/usr/bin/env python3
"""
File: 0-app.py
Desc: A simple flask application
Author: Gizachew Bayness
Date Created: Feb 28, 2023
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Handles the home route of the flask application"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
