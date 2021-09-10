from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

def init_db(app):
    db.app = app
    db.init_app(app)
    #db.create_all()

class Cars(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    maker = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    manufacture_year = db.Column(db.String, nullable=False)
    engine_displacement = db.Column(db.String, nullable=False)
    engine_power = db.Column(db.String, nullable=False)
    color_slug = db.Column(db.String, nullable=False)
    transmission = db.Column(db.String, nullable=False)
    door_count = db.Column(db.Integer, nullable=False)
    seat_count = db.Column(db.Integer, nullable=False)
    fuel_type = db.Column(db.String, nullable=False)
    price_eur = db.Column(db.Float, nullable=False)

    def __init__(self, maker, model, mileage, manufacture_year, engine_displacement, engine_power, color_slug,
                 transmission, door_count, seat_count, fuel_type, price_eur):
        self.maker = maker
        self.model = model
        self.mileage = mileage
        self.manufacture_year = manufacture_year
        self.engine_displacement = engine_displacement
        self.engine_power = engine_power
        self.color_slug = color_slug
        self.transmission = transmission
        self.door_count = door_count
        self.seat_count = seat_count
        self.fuel_type = fuel_type
        self.price_eur = price_eur

    @classmethod
    def get_distinct_values(self, column):
        return [row[0] for row in db.session.query(column).distinct().all()]

    @classmethod
    def get_min_value(self, column):
        return db.session.query(func.min(column)).all()

    @classmethod
    def get_max_value(self, column):
        return db.session.query(func.max(column)).all()


