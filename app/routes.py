from flask import render_template, request, flash
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.forms import PredictionRequestForm
from app.models import PredictionRequest


# create the first route
@app.route("/", methods=['GET', 'POST'])
def index():
    # initate the form
    form = PredictionRequestForm()
    
    
    # check the type of request
    if request.method == "POST":
        # get the data from the form
        data = request.form

        # add the data to the Prediction request
        prediction_request = PredictionRequest(username="test",
                                               country_code=data['country_code'].upper().strip(),
                                               city=data['city'].capitalize().strip())
        
        # add the data to the database
        try:
            db.session.add(prediction_request)

            # commit the change
            db.session.commit()
            flash(f"Succesfully added <b>{data['country_code']} - {data['city']}</b>", "success")
        except IntegrityError:
            db.session.rollback()
            flash(f"Combination <b>{data['country_code']} - {data['city']}</b> already exists", "danger")


    return render_template("index.html",
                           form = form)