from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=["POST"])
def search():
    query = request.form['query']
    return redirect(url_for('results', query=query))

@app.route("/results/<query>")
def results(query):
    search_url = f'https://www.google.com/search?q={query}'
    response = requests.get(search_url)
    return response.text

if __name__ == "_main_":
    app.run()