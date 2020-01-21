from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('home.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return redirect(url_for('login'))


# ======== Main ============================================================== #
if __name__ == "__main__":
    app = Flask(__name__, template_folder='templates')
    app.run(debug=True, use_reloader=True)
