from flask import Flask, render_template,request
app = Flask(__name__)
username = ""
password = ""
@app.route('/login')
def index():
    return render_template('index.html')
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    return username
if __name__ == '__main__':
    app.run(debug=True)
