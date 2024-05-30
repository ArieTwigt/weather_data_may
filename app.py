from flask import Flask, render_template


# initate a flask app
app = Flask(__name__)


# create the first route
@app.route("/")
def index():
    pass
    return render_template("index.html")


# launch the application
if __name__ == "__main__":
    app.run()