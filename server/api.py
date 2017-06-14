#!./bin/python3

from flask import Flask, request, send_from_directory, jsonify, make_response, abort
import os
import requests
from flask_cors import CORS, cross_origin
from collections import Counter
import datetime
import json
import sqlite3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from models import Base, engine, FeatureRequest


app = Flask(__name__, static_url_path='')
CORS(app)

Session = sessionmaker(bind=engine)

# app.run(debug=True)

@app.route('/submitFeatureRequest', methods=['POST'])
def submitFeatureRequest():
    session = Session()
    feature_req_priority = int(request.form['client_priority'])
    feature_date = datetime.datetime.strptime(request.form['date'], '%m/%d/%Y')
    session.query(FeatureRequest).\
        filter(FeatureRequest.client == request.form['client']).filter(FeatureRequest.client_priority >= feature_req_priority).\
        update({FeatureRequest.client_priority: FeatureRequest.client_priority + 1})
        # from_statement(text("Update feature_requests set client_priority = client_priority + 1 where client=:client and client_priority >= :client_priority")).\
        # params(client=request.form['client'], client_priority=feature_req_priority)

    feature_request = FeatureRequest(title=request.form['title'], description=request.form['description'],
        client=request.form['client'], product_area=request.form['product_area'], client_priority=feature_req_priority, date=feature_date)
    session.add(feature_request)
    session.commit()
    return make_response(jsonify({"error": "Merchant ID not given"}, 404))

@app.route('/getFeatureRequests', methods=['GET'])
def getFeatureRequests():
    session = Session()
    result = []
    for feature in session.query(FeatureRequest).order_by(text('client_priority')).all():
        result.append({'title': feature.title, 'description': feature.description,
            'client_priority': feature.client_priority, 'client': feature.client, 'product_area': feature.product_area,
            'date': feature.date.strftime('%m/%d/%Y'), 'id': feature.id})
    return make_response(jsonify(result))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
  #app.run(debug=True, threaded=True)
