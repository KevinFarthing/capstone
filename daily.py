from reddit_scrape import reddit_scrape
from pgconnect import connect
from psycofunctions import drop_old

connect(drop_old)
reddit_scrape()
