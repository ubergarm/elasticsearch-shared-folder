#!/usr/bin/python

from flask import Flask, render_template, url_for
from flask import Response
import json, os, datetime
from pyes import *

app = Flask(__name__)

## home dir
@app.route('/')
def home():
    return render_template('home.html')

## search post function to catch browser reload
@app.route('/search', methods = ['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_text', query = g.search_form.search.data))

## search parsedtext
@app.route('/search_text/<query>')
def search_text(query):
    conn = ES('127.0.0.1:9200')
    conn.default_indices=['files-index']
    q = MatchQuery('parsedtext', query)
    results = conn.search(query = q)
    return render_template('search_results.html',
                            query = q,
                            results = results)

## search filename
@app.route('/search_name/<query>')
def search_name(query):
    conn = ES('127.0.0.1:9200')
    conn.default_indices=['files-index']
    q = WildcardQuery('filename', query)
    results = conn.search(query = q)
    return render_template('search_results.html',
                            query = q,
                            results = results)

## handle 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
