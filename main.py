from flask import Flask,request,render_template
#import requests
import random
#pip install flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/coinflip")
def coinflip():
    return render_template("coinflip.html")

@app.route("/coinData")
def coinData():
    rnd = random.randint(0,1)
    return["TAILS","HEADS"][rnd]

    return render_template("coin.html")


@app.route("/randomQuote")
def randomQuote():
    return render_template("randomQuote.html")

@app.route("/Quotedata")
def Quotedata():
   
    rnd = random.randint(0,1)
    return["TAILS","HEADS"][rnd]

    return render_template("quote.html")

app.run(debug = True)