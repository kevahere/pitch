from flask import render_template
from . import main
@main.route('/')
def index():
    """View root function that returns index"""
    title =  'Home | welcome to pitches'
    return render_template('index.html', title = title)