from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))
        
    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    Analyzer(positives = "positive-words.txt", negatives = "negative-words.txt")

    for tweet in tweets:
        words = tweet.lower().split(" ")
        score = 0
        for word in words:
            if word.lower() in Analyzer.positive_words:
                score += 1
            elif word.lower() in Analyzer.negative_words:
                score -= 1
            else: 
                score = score

    positive = 0    
    negative = 0
    neutral = 0
    
    if score > 0.0:
        positive += 1
    elif score < 0.0:
        negative += 1
    else:
        neutral +=1
        
    total = (positive + negative + neutral)
    posititve = (positive/total) * 100
    negative = (negative/total) * 100
    neutral = (neutral/total) * 100
    print(positive)
    print(negative)
    print(neutral)
    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
