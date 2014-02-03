__author__ = 'pavan'
import praw
from pprint import pprint
import traceback
user_agent = ('exporting subreddits from one username to another username v1.0 by /u/91_pavan')
r = praw.Reddit(user_agent=user_agent)
username = '91_pavan'
password = ''
r.login(username, password)
x = r.get_my_subreddits()
alist = []
for i in x:
	alist.append(i)

#print list
user_agent1 = ('exporting subreddits from one username to another username v1.0 by /u/icutyouwithmmyknife')
r1 = praw.Reddit(user_agent = user_agent1)
username1 = 'icutyouwithmyknife'
password1 = ''
r1.login(username1, password1)

try:
    for i in alist:
    	r1.subscribe(str(i))
except Exception,e:
	print str(e)

print "All Done!"
