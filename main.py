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


    #print(request.args["vrednost"])    
    rnd = random.randint(0,1)
    status = ["TAILS", "HEADS"][rnd]
    if status == "HEADS":
        url = "https://i.postimg.cc/CBNJNfDJ/head.png"
    else:
        url = "https://i.postimg.cc/zysdXN8w/tail.png" 

    return {"img": url, "status": status}

    return render_template("coin.html")


@app.route("/randomQuote")
def randomQuote():
    return render_template("randomQuote.html")

@app.route("/Quotedata")
def Quotedata():
    quotes = [
        {"quote": "Life is what happens when you’re busy making other plans.", "author": "John Lennon"},
        {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
        {"quote": "The journey of a thousand miles begins with one step.", "author": "Lao Tzu"},
        {"quote": "Believe you can and you’re halfway there.", "author": "Theodore Roosevelt"},
        {"quote": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky"},
        {"quote": "Don’t count the days, make the days count.", "author": "Muhammad Ali"},
        {"quote": "Be the change that you wish to see in the world.", "author": "Mahatma Gandhi"},
        {"quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.", "author": "Zig Ziglar"},
        {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {   "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"}
    
    ]   

    izbran = random.choice(quotes)
    return izbran


@app.route("/randomNum")
def randomNum():
        return render_template("randomNum.html")



@app.route("/Numdata")
def Numdata():
    min=1
    max=30
    number = random.randint(min,max)
    return ((f"Number {naključno_število} Min {min} Max {max}"))

app.run(debug = True)