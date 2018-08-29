from app import app
from flask import render_template
from psycofunctions import get_story, get_full_list, get_random_story
from pgconnect import connect

@app.route('/')
@app.route('/index')
def index():
    story = connect(get_full_list)
    return render_template('index.html',story=story)

@app.route('/random')
def random():
    story = connect(get_random_story)
    return render_template('story.html',story=story)

@app.route('/storyid/<id>')
def story(id):
    story = connect(get_story,id)
    return render_template('story.html',story=story)

# heroku pg:push writing_prompt DATABASE_URL --app farthing-reddit-scraper
# pg:push causes env error due to calling sub functions in ubuntu format. switched to backup from hosted .dump