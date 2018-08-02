from reddit_scrape import reddit_scrape
from pgconnect import connect
from psycofunctions import get_ids

ids = connect(get_ids)
print(len(ids))
