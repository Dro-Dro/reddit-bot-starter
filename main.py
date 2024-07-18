import praw
import pdb
import re
import os

#creates instance of reddit
reddit = praw.Reddit('bot1')

#creates an empty list if it does not exist
if not os.path.isfile("posts_replied_to.txt") :
    posts_replied_to = []
#if it exists, then loads the list of replied to posts
else :
    with open("posts_replied_to.txt", "r") as f :
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

#grabs the top 5 'hot' posts from the subreddit
for submission in reddit.subreddit("pythonforengineers").hot(limit = 5) : 

    #if the post has not been replied to before
    if submission.id not in posts_replied_to :

        #if post contains key phrase; also ignores capitalization
        if re.search("i love python", submission.title, re.IGNORECASE) :
            #reply to post
            submission.reply("My Bot says: Me too!! ^_^")
            print("Bot replying to : ", submission.title)
            #save post id to list
            posts_replied_to.append(submission.id)

#write the updated list back onto file
with open("posts_replied_to.txt", "w") as f :
    for post_id in posts_replied_to : 
        f.write(post_id + "\n")