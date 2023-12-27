from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
import csv
import requests
import os
import json

load_dotenv()

app = Flask(__name__, static_url_path="/static")

with open("processed_senators.json", "r") as infile:
    data = json.load(infile)
    

@app.route("/")
def home():
    return render_template("pages/dailysummary.html", data=data)


@app.route("/official")
def dashboard():
    official = request.args.get("official")
    return render_template("pages/dashboard.html", official=official, data=data)

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/forum")
def forum():
    return render_template("pages/forum.html")

@app.route("/overview")
def overview():
    return render_template("pages/overview.html")

@app.route("/lesson1.html")
def lesson1():
    return render_template("pages/lesson1.html") 

@app.route("/lesson2.html")
def lesson2():
    return render_template("pages/lesson2.html") 

@app.route("/lesson3.html")
def lesson3():
    return render_template("pages/lesson3.html") 

@app.route("/lesson4.html")
def lesson4():
    return render_template("pages/lesson4.html") 

@app.route("/U2quiz.html")
def U2quiz():
    return render_template("pages/U2quiz.html") 

@app.route("/U2L1.html")
def U2L1():
    return render_template("pages/U2L1.html") 

@app.route("/U2L2.html")
def U2L2():
    return render_template("pages/U2L2.html") 

@app.route("/U2L3.html")
def U2L3():
    return render_template("pages/U2L3.html") 

@app.route("/U2L4.html")
def U2L4():
    return render_template("pages/U2L4.html") 

@app.route("/U2L5.html")
def U2L5():
    return render_template("pages/U2L5.html") 

@app.route("/forumcbai.html")
def forumcbai():
    return render_template("pages/forumcbai.html") 

@app.route("/forummburry.html")
def forummburry():
    return render_template("pages/forummburry.html") 

@app.route("/forumrjiang.html")
def forumrjiang():
    return render_template("pages/forumrjiang.html") 

@app.route("/forumvyao.html")
def forumvyao():
    return render_template("pages/forumvyao.html") 



if __name__ == "__main__":
    app.run(debug=True)
