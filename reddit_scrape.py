from psycofunctions import add_story, get_story, drop_old, get_titles
from pgconnect import connect
from login import reddit_config
import praw
import random



# connect to the PostgreSQL server



# refactor this. it's a mess.
def reddit_scrape():
    print('Connecting to Reddit...')
    params = reddit_config()
    with praw.Reddit(**params) as reddit:
        sub = reddit.subreddit("WritingPrompts")
        posts = [post for post in sub.top(time_filter="day", limit=10)]
        sql_entries = connect(get_titles)
        for post in posts:
            prompt_name = post.title.replace("'","''")
            if "[WP]" in prompt_name and prompt_name not in sql_entries:
                connect(add_story,[str(post.author),prompt_name,str(post.comments[1].author),post.comments[1].body.replace("'","''"),post.id])

