from app import app
from flask import render_template
from psycofunctions import get_story
from pgconnect import connect

@app.route('/')
@app.route('/index')
def index():
    # any variables?
    # user = {"don't need":"ain't gonna"}
    # yeah, actually. think i do need to run the connection(getstory) function here and assign it to a variable
    story = connect(get_story)
    return render_template('index.html',prompt_author=story[1],story_author=story[2],prompt_text=story[3],story_text=story[4],uber_id=story[0],prompt_url=story[5])