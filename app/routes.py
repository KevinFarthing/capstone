from app import app
from flask import render_template
from psycofunctions import get_story
from pgconnect import connect

@app.route('/')
@app.route('/index')
def index():
    story = connect(get_story)
    return render_template('index.html',story=story)

# heroku pg:push writing_prompt DATABASE_URL --app farthing-reddit-scraper