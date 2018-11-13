from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route('/data/', methods=['GET'])
def date():
	return str(datetime.now())

if __name__ == '__main__':
    app.run(debug=True)
