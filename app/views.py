from app import app, db
from flask import send_file, jsonify
from app.models import Stimmen, Gebiete
from app.schema import countries_schema


@app.route('/', methods=['GET', 'POST'])
def index():
    return send_file('templates/index.html')


@app.route('/api/countries', methods=['GET'])
def get_countries():
    countries = Gebiete.query.filter(Gebiete.belongs_to == 99)
    return jsonify(countries=countries_schema.dump(countries).data)


@app.route('/api/countries/<int:wahlkreis_id>', methods=['GET'])
def get_wahlkreise(wahlkreis_id):
    wahlkreise = Gebiete.query.filter(Gebiete.belongs_to == wahlkreis_id)
    return jsonify(wahlkreise=countries_schema.dump(wahlkreise).data)
