from app import app, db
from flask import send_file, jsonify
from app.models import Stimmen, Gebiete
from app.schema import countries_schema


@app.route('/home', methods=['GET', 'POST'])
def index():
    return send_file('templates/index.html')


@app.route('/api/countries', methods=['GET'])
def get_countries():
    countries = Gebiete.query.filter(Gebiete.belongs_to == 99)
    return jsonify(countries=countries_schema.dump(countries).data)
