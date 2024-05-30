from flask import Flask


# initate a flask app
app = Flask(__name__)


# create the first route
@app.route("/")
def index():
    pass
    return "Hello world!"


# launch the application
if __name__ == "__main__":
    app.run()