#!/usr/bin/env python3
import time
import sys
from termcolor import colored
from twython import Twython


# TODO
user_name = sys.argv[1]
if len(sys.argv) != 2:
    print("Usage: ./tweets @screen_name")
    exit(1)
    
CONSUMER_KEY = 'HSNEYzQiHOLfWQIlO60Qvi6eS'
CONSUMER_SECRET = 'lEunzYReHIba0GbQvNNUQ8LQOrb8udAJXAEESOsaehNhlGQ51c'
ACCESS_KEY = '830127596851568640-UVpc5Z0PsQaT3sSWtYZhz7VNvJUwJzP'
ACCESS_SECRET = 'Um7Gq4y9TbqNt2H5tQPOXrW3CxOETt7HwpH3dlrjfNyPD'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

for i in range(0, 1): 
    user_timeline = twitter.get_user_timeline(screen_name=user_name,count=50,include_retweets=False)
  

positive_words = []
negative_words = []

    
for line in open("negative-words.txt"):
    li = line.strip()
    if not li.startswith(";"):
        negative_words.append(li)

for line in open("positive-words.txt"):
    li = line.strip()
    if not li.startswith(";"):
        positive_words.append(li)
            
for tweet in user_timeline:
    score = 0
    words = tweet['text'].lower().split(" ")

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    
    if score > 0:
        print(colored(str(score)+' '+tweet['text'], "green"))
    elif score < 0:
        print(colored(str(score)+' '+tweet['text'], "red"))
    else:
        print(colored(str(score)+' '+tweet['text'], "yellow"))
