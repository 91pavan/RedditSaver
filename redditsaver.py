__author__ = 'pavan'
import praw
from pprint import pprint

user_agent = ('exporting saved links from one username to another username v1.0 by /u/91_pavan')
r = praw.Reddit(user_agent=user_agent)
username = '91_pavan'
password = ''
r.login(username, password)
saved_links = r.user.get_saved(limit=50)
for x in saved_links:
    print str(x.url)

