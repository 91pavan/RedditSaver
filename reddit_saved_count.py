__author__ = 'pavan'
import praw
from pprint import pprint
import traceback
user_agent = ('exporting saved links from one username to another username v1.0 by /u/91_pavan')
r = praw.Reddit(user_agent=user_agent)
username = '91_pavan'
password = ''
r.login(username, password)
saved_links = r.user.get_saved(limit=None)
count = 0
for x in saved_links:
   count+=1

print "91_pavan " + str(count)
#post = iter(saved_links)
#list = []
#try:
 #   for i in post:
 #       list.append(i.id)
#except Exception, e:
 #   traceback.print_exc()
    #list.append(i.id)

#print list


#print list
user_agent1 = ('exporting saved links from one username to another username v1.1 by /u/icutyouwithmmyknife')
r1 = praw.Reddit(user_agent = user_agent1)
username1 = 'icutyouwithmyknife'
password1 = 'counterstrike'
r1.login(username1, password1)

saved_links = r1.user.get_saved(limit=None)
count1 = 0
for x in saved_links:
   count1+=1

print "icutyouwithmyknife " + str(count1)


#for entry in list:
#    submission = r1.get_submission(url=None, submission_id=entry, comment_limit=0, comment_sort=None)
#    submission.save()


print "All Done!"
