from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import time
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///contacts.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
localtime = time.asctime(time.localtime(time.time()))

class contactRequests(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(256), nullable = False)
    just = db.Column(db.String(1000), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.UTC)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about me')
def about_page():
    return render_template("about.html")

if __name__ == '__main__':

    app.run(debug=True, port=5050)