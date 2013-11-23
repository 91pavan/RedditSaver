__author__ = 'pavan'
import praw

user_agent = ('exporting saved links from one username to another username v1.0 by /u/91_pavan')
r = praw.Reddit(user_agent=user_agent)
r.login('91_pavan', 'xxxxxxxxx')
saved_links = r.user.get_saved(limit=None)


for x in saved_links:
    print x
