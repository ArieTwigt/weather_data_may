from flask import render_template, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.forms import PredictionRequestForm
from app.models import PredictionRequest
from app.utils.weather import get_weater_data


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

    # get all the saved prediction requests
    prediction_requests = PredictionRequest.query.all()

    return render_template("index.html",
                           form = form,
                           prediction_requests=prediction_requests)


# route for modifying an existing prediction request
@app.route('/edit_prediction_request/<id>', methods=['GET', 'POST'])
def edit_prediction_request(id):
    # get the prediction request with the given id
    prediction_request = PredictionRequest.query.get(id)

    # render the form
    form = PredictionRequestForm(obj=prediction_request)

    # if we get a post request
    if request.method == 'POST':
        # get the data form the form
        data = form.data
        
        # modify the prediction_request
        prediction_request.city = data['city']
        prediction_request.country_code = data['country_code']

        # commit the changes
        db.session.commit()

        # return to the index
        flash("Succesfully modified", "success")
        return redirect(url_for('index'))

    return render_template("edit_prediction_request.html",
                           form=form)

    
# route for getting the weather data
@app.route('/get_weather_data/<id>')
def get_weather_data(id):
    # get the id
    prediction_request = PredictionRequest.query.get(id)

    # get the city from the prediction_request
    city = prediction_request.city

    # use the function to get the data from the city
    predictions_dict = get_weater_data(city)

    # get the form
    form = PredictionRequestForm()

    # get the prediction requests
    prediction_requests = PredictionRequest.query.all()

    return render_template("index.html", 
                           form=form, 
                           prediction_requests=prediction_requests,
                           predictions_dict=predictions_dict)