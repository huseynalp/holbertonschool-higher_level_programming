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


# ============================================================================
# TEMPLATES - Create these files in a 'templates' folder
# ============================================================================

# templates/header.html
"""
<header>
    <h1>My Flask App</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/contact">Contact</a>
    </nav>
</header>
<hr>
"""

# templates/footer.html
"""
<hr>
<footer>
    <p>&copy; 2024 My Flask App</p>
</footer>
"""

# templates/index.html
"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask App - Home</title>
</head>
<body>
    {% include 'header.html' %}
    
    <main>
        <h1>Welcome to My Flask App</h1>
        <p>This is a simple Flask application.</p>
        <ul>
            <li>Flask</li>
            <li>HTML</li>
            <li>Templates</li>
        </ul>
    </main>
    
    {% include 'footer.html' %}
</body>
</html>
"""

# templates/about.html
"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask App - About</title>
</head>
<body>
    {% include 'header.html' %}
    
    <main>
        <h1>About Us</h1>
        <p>This is the about page. Here you can learn more about our Flask application and its features. We demonstrate the use of Jinja templates with reusable header and footer components.</p>
    </main>
    
    {% include 'footer.html' %}
</body>
</html>
"""

# templates/contact.html
"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask App - Contact</title>
</head>
<body>
    {% include 'header.html' %}
    
    <main>
        <h1>Contact Us</h1>
        <p>Get in touch with us! You can reach us through various channels. We'd love to hear from you about your experience with our Flask application.</p>
    </main>
    
    {% include 'footer.html' %}
</body>
</html>
"""
