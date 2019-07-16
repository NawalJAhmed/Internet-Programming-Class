from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

import sys
sys.path.insert(0, 'db_util')
from db_util.db_help import *


app = Flask(__name__)
api = Api(app)
        

class Get_all_areas(Resource):
    def get(self):
        return get_all_areas()

class Get_locations_for_area(Resource):
    def get(self, area):
        return get_locations_for_area( area )

class Get_measurements_for_location(Resource):
    def get(self, location):
        return get_measurements_for_location( location) 

class Get_categories_for_area(Resource):
    def get(self, area):
        return get_categories_for_area(area)

class Get_average_measurement_for_area(Resource):
    def get(self, area):
        return get_average_measurement_for_area(area)

class Get_number_of_locations_in_area(Resource):
    def get(self, area):
        return get_number_of_locations_in_area(area)

api.add_resource(Get_all_areas, '/area') # Route_1
api.add_resource(Get_locations_for_area, '/area/<int:area>/location') # Route_2
api.add_resource(Get_measurements_for_location, '/location/<int:location>/measurement') # Route_3
api.add_resource(Get_categories_for_area, '/area/<int:area>/category') # Route_4
api.add_resource(Get_average_measurement_for_area, '/area/<int:area>/average_measurement') # Route_5
api.add_resource(Get_number_of_locations_in_area, '/area/<int:area>/number_locations') # Route_6


if __name__ == '__main__':
     app.run(port='12345')
