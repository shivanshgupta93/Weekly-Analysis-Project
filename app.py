import os
from flask import Flask, render_template
from routes import api

app = Flask(__name__, template_folder='static')

app.register_blueprint(api)

@app.route("/")

def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
