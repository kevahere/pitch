from flask import render_template

@main.route('/')
def index():
    """View root function that returns index"""
    return render_template('index.html')