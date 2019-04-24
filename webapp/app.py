#!/usr/bin/env python

from flask import Flask, render_template, Response, redirect, url_for, request, session, flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


