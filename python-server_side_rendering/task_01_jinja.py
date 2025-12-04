#!/usr/bin/python3
"""
task_01_jinja.py

A basic Flask application demonstrating Jinja templating with reusable components.
This application includes multiple pages with shared header and footer templates.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
