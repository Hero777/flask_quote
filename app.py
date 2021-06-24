from flask import Flask, render_template
from data import data

import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/quote")
def quote():
    citation = random.choice(data)
    return render_template('quote.html', citation=citation)


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()
