import praw

reddit = praw.Reddit('bot1')
subReddit = reddit.subreddit("learnpython")

for submission in subReddit.hot(limit = 5) : 
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("--------------------------------\n")