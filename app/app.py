from flask import Flask, render_template, request

from app.models.models import Cars
from .models import models

app = Flask(__name__)
app.config.from_object('config')
models.init_db(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form', methods=["POST", "GET"])
def form():
    if request.method == "POST":
        maker_choice = request.form.getlist("maker")
        model_choice = request.form.getlist("model")
        # mileage_choice = request.form.getlist("mileage")
        data = Cars.get_where_conditions(maker=maker_choice, model=model_choice)
        return render_template("results.html", data=data)
    else:
        car_maker = Cars.get_distinct_values(Cars.maker)
        car_models = Cars.get_distinct_values(Cars.model)
        car_mileage = [Cars.get_min_value(Cars.mileage), Cars.get_max_value(Cars.mileage)]
        car_year = [Cars.get_min_value(Cars.manufacture_year), Cars.get_max_value(Cars.manufacture_year)]

        # engine_displacement = db.Column(db.String, nullable=False)
        # engine_power = db.Column(db.String, nullable=False)
        # color_slug = db.Column(db.String, nullable=False)
        # transmission = db.Column(db.String, nullable=False)
        # door_count = db.Column(db.Integer, nullable=False)
        # seat_count = db.Column(db.Integer, nullable=False)
        # fuel_type = db.Column(db.String, nullable=False)
        # price_eur = db.Column(db.Float, nullable=False)

        return render_template('form.html', makers=car_maker, models=car_models, mileage=car_mileage, years=car_year)


if __name__ == '__main__':
    app.run()
