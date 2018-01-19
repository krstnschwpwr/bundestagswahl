#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app, db
from flask import send_file, jsonify
from app.models import Stimmen, Gebiete, Parteien
from app.schema import countries_schema, details_schema, parteien_schema


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
    # details = Stimmen.query.filter(Stimmen.id == wahlkreis_id)
    return jsonify(wahlkreise=countries_schema.dump(wahlkreise).data)


@app.route('/api/countries/detail/<int:wahlkreisDetailId>', methods=['GET'])
def get_details(wahlkreisDetailId):
    tmpparteien = Parteien.query.all()
    tmpdetails = Stimmen.query.filter(Stimmen.id == wahlkreisDetailId)
    details = details_schema.dump(tmpdetails).data
    fixeddetails = []
    parteien = parteien_schema.dump(tmpparteien).data
    for detail in details[0]:
        if detail != "id":
            parteiid = detail[1:].split('_')
            for partei in parteien:
                if partei.get('id') == int(parteiid[0]):
                    fixeddetails.append([partei.get('name') + " " + getvotetype(int(parteiid[1])), details[0].get(detail)])

    return jsonify(sorted(fixeddetails, key=lambda x: x[0]))


def getvotetype(argument):
    switcher = {
        0: u"Erststimmen Vorläufig",
        1: u"Erststimmen Vorperiode",
        2: u"Zweitstimmen Vorläufig",
        3: u"Zweitstimmen Vorperiode"
    }
    return switcher.get(argument, "default")
