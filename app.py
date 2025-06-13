# app.py
from flask import Flask, render_template
from backend import get_headlines

app = Flask(__name__)

@app.route('/')
def index():
    headlines = get_headlines()
    return render_template('website.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
