__author__ = 'Gaurav-PC'

import csv
from flask import Flask
from flask import jsonify
from pprint import pprint
from flask import send_file
from flask import make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
version = 'v1'

italian_timeline_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\italy\\italian_aggregate_years.csv"
chinese_timeline_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\china\\chinese_aggregate_years.csv"
indian_timeline_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\india\\indian_aggregate_years.csv"
mideast_timeline_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\mideast\\mideast_aggregate_years.csv"

italian_geo_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\italy\\italian_aggregate_countries.csv"
chinese_geo_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\china\\chinese_aggregate_countries.csv"
indian_geo_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\india\\indian_aggregate_countries.csv"
mideast_geo_file = "F:\\SOIC Courses\\Big Data\\Final Project\\Cuisine-Dataset\\locations\\final\\mideast\\mideast_aggregate_countries.csv"

cors = CORS(app, resources={r"/lta/*": {"origins": "localhost"}})

@app.route('/lta/'+version+'/aggregation/years/<string:cuisine>', methods=['GET'])
@cross_origin(origin='localhost')
def get_aggregation_years(cuisine):
    filename = eval(cuisine + '_file')

    with open(filename, 'rb') as fp:
        reader = csv.reader(fp)

        data = []
        for row in reader:
            data.append(row)

        pprint(data)

        return jsonify({
            'data': data
        })

@app.route('/lta/'+version+'/aggregation/timeline/file/<string:cuisine>', methods=['GET'])
@cross_origin(origin='localhost')
def get_timeline_file(cuisine):
    filename = eval(cuisine + '_timeline_file')
    return send_file(filename,
                     mimetype='text/csv',
                     attachment_filename='timeline.csv',
                     as_attachment=True)

@app.route('/lta/'+version+'/aggregation/geo/file/<string:cuisine>', methods=['GET'])
@cross_origin(origin='localhost')
def get_geo_file(cuisine):
    filename = eval(cuisine + '_geo_file')
    return send_file(filename,
                     mimetype='text/csv',
                     attachment_filename='geo.csv',
                     as_attachment=True)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)