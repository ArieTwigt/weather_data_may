from flask import render_template
from app import app

# create the first route
@app.route("/")
def index():
    pass
    return render_template("index.html")